function render_dream() {
    let node = document.getElementById("dreams-enclosure")
    let dreams = [ /* GET DREAMS ENDPOINT */
        { 
            title: "Sonho Mockado",
            text: "Sonho onde ocorreu um dado sonho sonhado...",
            tags: ["Fulano", "Felicidade", "Paz"]
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

        let tags = document.createElement("div")
        tags.className = "dream-tags"

        dream.tags.forEach(tag => {
            let tag_node = document.createElement("p")
            tag_node.innerText = tag
            tag_node.className = "dream-tag"

            tags.appendChild(tag_node)
        })

        dream_node.appendChild(title)
        dream_node.appendChild(text)
        dream_node.appendChild(tags)

        node.appendChild(dream_node)
    })
}

render_dream()