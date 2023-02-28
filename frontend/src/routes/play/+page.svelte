<script lang="ts">
    import Card from "../../components/Card.svelte"
    import Navbar from "../../components/Navbar.svelte"
    import Button from "../../components/Button.svelte"

    var suits = ["spades", "diamonds", "clubs", "hearts"];
    var values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"];
    var start_cards = 6;
    var trumpCard = 0;

    export let deck = shuffle(getDeck());
    export let dead_deck = [];
    export let bot_cards = [];
    export let player_cards = [];
    export let field_cards = [];

    setupGame(deck);

    function getDeck() {
        let deck = new Array();
        for(let i = 0; i < suits.length; i++) {
            for(let x = 0; x < values.length; x++) {
                let card = {Value: values[x], Suit: suits[i]};
                deck.push(card);
            }
        }
        return deck;
    }

    function shuffle(deck) {
        // switch the values of two random cards per iteration
        for (let i = 0; i < deck.length; i++) {
            let location1 = Math.floor((Math.random() * deck.length));
            let location2 = Math.floor((Math.random() * deck.length));
            let tmp = deck[location1];

            deck[location1] = deck[location2];
            deck[location2] = tmp;
        }

        return deck;
    }

    function removeCardFromDeck(_deck, card) {
        dead_deck = [...dead_deck, card]
        _deck.forEach(function(item, index, object) {
            if (item === card) {
                console.log("------")
                console.log("Suit: " + item["Suit"])
                console.log("Value: " + item["Value"])
                console.log("Index: ", index)
                _deck.splice(index, 1);
                // Removes the right element from deck but only removes the last element from the player_hand
            }
        });

        return _deck;
    }

    function getRandomCard(deck) {
        let card = deck[Math.floor(Math.random() * deck.length)];
        removeCardFromDeck(deck, card);

        return card;
    }

    function setupGame(deck) {
        let trump = getRandomCard(deck);
        trumpCard = trump

        for (let i=0; i<start_cards; i++) {
            bot_cards.push(getRandomCard(deck))
        };

        for (let i=0; i<start_cards; i++) {
            player_cards.push(getRandomCard(deck))
        };

        botMove();
    }

    function takeCards(bot) {
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

    function stackUpDeck(_deck) {
        if (_deck.length !== start_cards) {
            let missing = start_cards - deck.length;
            for (let i=0; i<missing; i++) {
                let card = getRandomCard(deck);
                deck = [...deck, card];
            }
        }
    }

    function endRound() {   // "TypeError: ctx[1] is undefined" somewhere from within this function
        let new_deck = stackUpDeck(bot_cards);
        bot_cards = new_deck;

        new_deck = stackUpDeck(player_cards);
        player_cards = new_deck;
    }

    function botMove() {
        if (field_cards.length === 0) {
            let card;
            if (field_cards.length > 1) {
                // If bot doesn't make first move check if one of field cards has same number as one of the bots cards
                for(let i=0; i<bot_cards.length; i++) {
                    for(let j=0; j<field_cards.length; j++) {
                        if(bot_cards[i]["Value"] === field_cards[j]["Value"]) {
                            card = bot_cards[i];
                            let new_deck = removeCardFromDeck(bot_cards, card);
                            bot_cards = new_deck;
                        }
                    }
                }
            } else {
                // If bot makes first move just add the first card from the deck to the field
                card = bot_cards[0];
                let new_deck = removeCardFromDeck(bot_cards, card);
                bot_cards = new_deck;
            }

            // Move card to field
            field_cards = [...field_cards, card];
        }
    };

    function moveValid(card) {
        let latest_card = field_cards[field_cards.length - 1];

        if (latest_card === undefined) {

            return true;
        } else {
            // Check if suit of defending card matches attacking card
            if (card["Suit"] === latest_card["Suit"]) {
                // Check if defending card is higher than attacking card or if defending card is ace while attacking card is not
                if (card["Value"] > latest_card["Value"] || card["Value"] === 1 && latest_card["Value"] !== 1) { 
                    return true;
                }
                console.log("Value is not greater! Not a trump card!")
                return false;

            } else if (card["Suit"] === trumpCard["Suit"]) {
                if (latest_card["Suit"] === trumpCard["Suit"]) {
                    if (card["Value"] > latest_card["Value"]) {
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

    function selectCard(card) {
        if (!(field_cards.length >= 6)) {
            if (moveValid(card)) {
                field_cards = [...field_cards, card];
                let new_deck = removeCardFromDeck(player_cards, card);
                player_cards = new_deck;

                botMove();
            } else {
                console.log("Not a valid move!");
            }
        }
    };
</script>

<Navbar></Navbar>

<div class="game container mx-auto px-4">
    <div class="grid grid-rows-3 grid-flow-col gap-3">
        <div class="enemy_hand border-2 border-black bg-sky-500 p-3">
            <div class="mx-auto text-4xl font-sans">Durak Bots Hand</div>
            {#each Array(bot_cards.length) as _, index}
                <!--<Card suit="cards" value="BACK" small={true}></Card>-->
                <Card small={true} suit={bot_cards[index]["Suit"]} value={bot_cards[index]["Value"]}></Card>
            {/each}
        </div>
        <div class="field border-2 border-black bg-red-800 p-3">
            <div class="relative float-right mr-4 mb-2 border-l-4 border-black px-2">
                <div class="absolute top-0 right-3 text-lg font-sans font-bold">Cards in deck: {deck.length}</div>
                <Card suit={trumpCard["Suit"]} value={trumpCard["Value"]}></Card>
                <Card suit="cards" value="BACK"></Card>
                <div class="container float-bottom mx-auto">
                    <Button on:click={() => takeCards(false)} title={"Take Cards"}></Button>
                    <Button on:click={() => endRound()} title={"Finish Round"}></Button>
                </div>
            </div>
            <div class="grid grid-flow-col-dense columns-6">
                {#each Array(field_cards.length) as _, index}
                    <Card suit={field_cards[index]["Suit"]} value={field_cards[index]["Value"]}></Card>
                {/each}
            </div>
        </div>
        <div class="player_hand border-2 border-black bg-sky-500 p-3">
            <div class="mx-auto text-4xl font-sans">Your Hand</div>
            {#each Array(player_cards.length) as _, index}
                <Card on:click={() => selectCard(player_cards[index])} small={true} bind:field={field_cards} suit={player_cards[index]["Suit"]} value={player_cards[index]["Value"]}></Card>
            {/each}
        </div>
    </div>
</div>