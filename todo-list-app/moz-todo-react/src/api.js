export async function getTodoList(){
    const response = await fetch("http://127.0.0.1:8000/todos")
    return await response.json()
}

export async function postTodo(name){
    const response = await fetch("http://127.0.0.1:8000/todos", {
        method: "POST", body: JSON.stringify({ name }), headers: {
            "content-type": "application/json"
        }
    })
}
