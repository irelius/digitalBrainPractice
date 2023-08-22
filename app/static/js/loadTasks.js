import React from "react"

function loadStorageTasks() {
    const localStorageTasks = localStorageGet("tasks")
    console.log('load tasks', localStorageTasks)
}

export default loadStorageTasks
