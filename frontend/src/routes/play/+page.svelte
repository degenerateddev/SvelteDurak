<script lang="ts">
    import type { GameCard } from "$lib/types";
    import Card from "../../components/Card.svelte"
    import Button from "../../components/Button.svelte"

    /*
    Game Rules:
        1. Pick trump card first
        2. Attacker picks a card from their own deck (deck of 6)
        3. Defender picks card with the same suit but a higher value than the Attackers card (or with same suit as trump card)
        4. By doing that, create a stack of two (Attacking card, defending card)
        5. Attacker can create a second stack by picking a card with the same value as another card already on the field
        6. If Defender can't defend, he has to take all cards on the field
        7. Once someone can't pick anymore, both players fill up their decks again (decks of 6) (Defender only if needed)
        8. The cards previously on the field get added to the "dead deck" (If Defender was able to defend)
        9. Once there are no cards left on the stack, it's about losing all owned cards first
        10. Whoever has no cards anymore, wins the game
        11. Attacker doesn't have to attack, Defender doesn't have to defend (even if they're able to)
    */

    var suits = ["spades", "diamonds", "clubs", "hearts"];
    var values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"];
    var start_cards = 6;
    var trumpCard: GameCard;

    export var main_deck: Array<GameCard> = shuffle(getDeck());  // All game cards
    export let dead_deck: Array<GameCard> = [];             // Cards out of the game
    export let bot_cards: Array<GameCard> = [];             // Cards of the computer
    export let player_cards: Array<GameCard> = [];          // Cards of the player
    export let field_cards: Array<GameCard> = [];           // Cards visible on the table right now

    setupGame(main_deck);

    function getDeck() {
        let deck: Array<GameCard> = [];
        for(let i = 0; i < suits.length; i++) {
            for(let x = 0; x < values.length; x++) {
                let card: GameCard = {suit: suits[i], value: Number(values[x])};
                deck.push(card);
            }
        }
        return deck;
    }

    function shuffle(deck: Array<GameCard>) {
        // switch the values of two random cards per iteration
        /*for (let i = 0; i < deck.length; i++) {
            let location1 = Math.floor((Math.random() * deck.length));
            let location2 = Math.floor((Math.random() * deck.length));
            let tmp = deck[location1];

            deck[location1] = deck[location2];
            deck[location2] = tmp;
        }*/
        for (let i = deck.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [deck[i], deck[j]] = [deck[j], deck[i]];
        }

        return deck;
    }

    function removeCardFromDeck(deck: Array<GameCard>, card: GameCard) {
        dead_deck = [...dead_deck, card]
        deck.forEach(function(item, index, object) {
            if (item === card) {
                console.log("------")
                console.log("Suit: " + item.suit)
                console.log("Value: " + item.value)
                console.log("Index: ", index)
                deck.splice(index, 1);
                // Removes the right element from deck but only removes the last element from the player_hand
            }
        });

        return deck;
    }

    function getRandomCard(deck: Array<GameCard>) { // to get the trump card before the game starts
        let card: GameCard = deck[Math.floor(Math.random() * deck.length)];
        removeCardFromDeck(deck, card);

        return card;
    }

    function setupGame(deck: Array<GameCard>) { // pick trump card and fill bot & player decks
        trumpCard = getRandomCard(deck);

        for (let i=0; i<start_cards; i++) {
            bot_cards.push(getRandomCard(deck))
        };

        for (let i=0; i<start_cards; i++) {
            player_cards.push(getRandomCard(deck))
        };

        botMove();  // bot always moves first
    }

    function takeCards(bot: boolean) {  // Add cards to deck of losing party
        if (bot) {
            // Bot lost and takes cards
            field_cards.forEach(element => {
                bot_cards = [...bot_cards, element];
                removeCardFromDeck(field_cards, element);
            });
            endRound();
        } else {
            // Player lost and takes cards
            field_cards.forEach(element => {
                player_cards = [...player_cards, element];
                removeCardFromDeck(field_cards, element);
            });
            endRound();
            botMove();
        }
    }

    function stackUpDeck(deck: Array<GameCard>) {
        if (!(deck.length >= start_cards) ) {  // maybe check if original deck still has enough cards?
            let missing = start_cards - deck.length;

            for (let i=0; i<missing; i++) {
                let card: GameCard = getRandomCard(main_deck);
                deck = [...deck, card];
            }

            return deck;
        }

        return null;
    }

    function endRound() {   // "TypeError: ctx[1] is undefined" somewhere from within this function
        let new_deck: Array<GameCard> | null = stackUpDeck(bot_cards);
        if (new_deck !== null) {
            bot_cards = new_deck;
        }

        new_deck = stackUpDeck(player_cards);
        if (new_deck !== null) {
            player_cards = new_deck;
        }
    }

    function botMove() {
        if (field_cards.length === 0) {
            let card: GameCard;
            if (field_cards.length > 1) {
                // If bot doesn't make first move check if one of field cards has same number as one of the bots cards
                for(let i=0; i<bot_cards.length; i++) {
                    for(let j=0; j<field_cards.length; j++) {
                        if(bot_cards[i].value === field_cards[j].value) {
                            card = bot_cards[i];
                            let new_deck = removeCardFromDeck(bot_cards, card);
                            bot_cards = new_deck;
                        }
                    }
                }
            } else {
                // If bot makes first move just add the first card from the deck to the field
                card = bot_cards[0];
                let new_deck: Array<GameCard> = removeCardFromDeck(bot_cards, card);
                bot_cards = new_deck;
            }

            // Move card to field
            field_cards = [...field_cards, card];
        }
    };

    function moveValid(card: GameCard) {
        let latest_card: GameCard = field_cards[field_cards.length - 1];

        if (latest_card === undefined) {

            return true;
        } else {
            // Check if suit of defending card matches attacking card
            if (card.suit === latest_card.suit) {
                // Check if defending card is higher than attacking card or if defending card is ace while attacking card is not
                if (card.value > latest_card.value || card.value === 1 && latest_card.value !== 1) { 
                    return true;
                }
                console.log("Value is not greater! Not a trump card!")
                return false;

            } else if (card.suit === trumpCard.suit) {
                if (latest_card.suit === trumpCard.suit) {
                    if (card.value > latest_card.value) {
                        return true;
                    }
                    console.log("Value is not greater! Trump card!")
                    return false;
                } else {
                    return true;
                }
            }
            console.log("Not a fitting suit or trump card suit!")
            return false;
        }
    }

    function selectCard(card: GameCard) {   // After clicking a card, check if move is valid and add to field
        if (field_cards.length < 6) { //!(field_cards.length >= 6)
            if (moveValid(card)) {
                field_cards = [...field_cards, card];
                let new_deck: Array<GameCard> = removeCardFromDeck(player_cards, card);
                player_cards = new_deck;

                botMove();
            } else {
                console.log("Not a valid move!");
            }
        }
    };
</script>

<div class="game container mx-auto px-4">
    <div class="grid grid-rows-3 grid-flow-col gap-3">

        <div class="enemy_hand border-2 border-black bg-sky-500 p-3">
            <div class="mx-auto text-4xl font-sans">Durak Bots Hand</div>
            {#each Array(bot_cards.length) as _, index}
                <Card small={true} suit={bot_cards[index].suit} value={bot_cards[index].value}></Card>
            {/each}
        </div>

        <div class="field border-2 border-black bg-red-800 p-3">
            <div class="relative float-right mr-4 mb-2 border-l-4 border-black px-2">
                <div class="absolute top-0 right-3 text-lg font-sans font-bold">Cards in deck: {main_deck.length}</div>
                <Card suit={trumpCard.suit} value={trumpCard.value}></Card>
                <Card suit="cards" value="BACK"></Card>
                <div class="container float-bottom mx-auto">
                    <Button on:click={() => takeCards(false)} title={"Take Cards"}></Button>
                    <Button on:click={() => endRound()} title={"Finish Round"}></Button>
                </div>
            </div>
            <div class="grid grid-flow-col-dense columns-6">
                {#each Array(field_cards.length) as _, index}
                    <Card suit={field_cards[index].suit} value={field_cards[index].value}></Card>
                {/each}
            </div>
        </div>

        <div class="player_hand border-2 border-black bg-sky-500 p-3">
            <div class="mx-auto text-4xl font-sans">Your Hand</div>
            {#each Array(player_cards.length) as _, index}
                <Card on:click={() => selectCard(player_cards[index])} small={true} bind:field={field_cards} suit={player_cards[index].suit} value={player_cards[index].value}></Card>
            {/each}
        </div>

    </div>
</div>