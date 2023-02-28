import type { PageLoad } from './$types';
 
export const load = (async ({ params }) => {
    const response = await fetch("http://127.0.0.1:8000/api/get-games", {
        method: "GET",
        headers: new Headers({
            "Accept": "application/json"
        })
    })

    if (response.ok) {
        const data = await response.json()
        console.log(data)
        return {
            games: data
        }
    }
    return {
        status: 500
    };
}) satisfies PageLoad;