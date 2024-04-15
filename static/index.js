
const createMatchForm = document.getElementById('create-match')
const joinMatchForm = document.getElementById('join-match')

const usernameToCreateInput = document.getElementById('username-to-create')
const usernameToJoinInput = document.getElementById('username-to-join')
const usernameOwnerOfMatchInput = document.getElementById('match-owner')

createMatchForm.addEventListener('submit', async (ev) => {
    ev.preventDefault()

    const username = usernameToCreateInput.value

    console.log(username)

    await fetch('/login', {
        method: 'POST',
        body: JSON.stringify({ username }),
        headers: {
            'Content-Type': 'application/json'
        }
    })

    await fetch('/create-match', {
        method: 'POST',
        body: JSON.stringify({ username }),
        headers: {
            'Content-Type': 'application/json'
        }
    })

    location.assign(`/match/${username}`)
})

joinMatchForm.addEventListener('submit', async (ev) => {
    ev.preventDefault()

    const username = usernameToJoinInput.textContent
    const owner = usernameOwnerOfMatchInput.textContent

    await fetch('/login', {
        method: 'POST',
        body: JSON.stringify({ username }),
        headers: {
            'Content-Type': 'application/json'
        }
    })

    await fetch('/join-match', {
        method: 'POST',
        body: JSON.stringify({ username }),
        headers: {
            'Content-Type': 'application/json'
        }
    })

    location.assign(`/match/${owner}`)
})