import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
 
export const load = (async (event) => {
    const response = await fetch("http://127.0.0.1:8000/api/get-games/", {
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