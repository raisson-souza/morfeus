function resizeCanvas(canvasId) {
    const canvas = document.getElementById(canvasId);
    const parentElement = canvas.parentElement;

    canvas.width = parentElement.offsetWidth;
    canvas.height = parentElement.offsetHeight;
}

function render_graph(canvas_id, labels, data, backgrounds) {
    const ctx = document.getElementById(canvas_id)

    if (data[0] + data[1] == 0) {
        let p_node = document.createElement("p")
        p_node.className = "no-graph-alert"
        p_node.innerHTML = "Nenhum sonho cadastrado."
        node = document.querySelector( 
            canvas_id == "pizza1"
                ? ".total-dream-nightmare-graph"
                : ".my-dream-nightmare-graph"
        )
        node.appendChild(p_node)
        ctx.remove()
        return
    }

    resizeCanvas(canvas_id)

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                label: 'Sonhos / Pesadelos',
                data: data,
                backgroundColor: backgrounds,
                hoverOffset: 4
            }]
        }
    })
}