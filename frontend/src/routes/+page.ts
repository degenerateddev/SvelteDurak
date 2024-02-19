import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import { API } from 'lib/env';
 
export const load = (async (event) => {
    const response = await fetch(API + "game/", {
        method: "GET",
        headers: new Headers({
            "Accept": "application/json"
        })
    })

    if (response.ok) {
        const data = await response.json()
        return {
            games: data
        }
    }

    throw error(500)

}) satisfies PageLoad;