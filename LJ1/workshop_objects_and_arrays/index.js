const main = document.querySelector('#main')

const data = [
    {"title": "Fake Title", "content": "nsljdhglkshgklhsdhsdg"},
    {"title": "Another Post", "content": "This is more sample content"},
    {"title": "Third Post", "content": "Even more blog content here"}
]

const createItem = (item) => {
    const div = document.createElement('div')
    const h1 = document.createElement('h1')
    const p = document.createElement('p')
    
    h1.textContent = item.title
    p.textContent = item.content
    
    div.appendChild(h1)
    div.appendChild(p)
    main.appendChild(div)
}

data.forEach(item => {
    createItem(item)
})
