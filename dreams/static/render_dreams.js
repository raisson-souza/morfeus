function render_dream() {
    let node = document.getElementById("dreams-enclosure")
    let dreams = [ /* GET DREAMS ENDPOINT */
        { 
            title: "Sonho Mockado",
            text: "Sonho onde ocorreu um dado sonho sonhado...",
        }
    ]

    dreams.forEach((dream, i) => {
        let dream_node = document.createElement("div")
        dream_node.className = "dream-node"

        let title = document.createElement("h3")
        title.className = "dream-title"
        title.innerText = dream.title

        let text = document.createElement("p")
        text.className = "dream-text"
        text.innerText = dream.text

        dream_node.appendChild(title)
        dream_node.appendChild(text)

        node.appendChild(dream_node)
    })
}

render_dream()