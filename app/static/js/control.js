function showBtn(group, btn_id){
    const btn = document.getElementById(`btn_${group}_${btn_id}`)
    btn.style.opacity = 1
}
    
function hideBtn(group, btn_id){
    const btn = document.getElementById(`btn_${group}_${btn_id}`)
    btn.style.opacity = 0
}

function displayError(message){
    $('#error-message').text(message)
    $('#error-box').modal('toggle')
}

function signUp(el){
    const input = document.getElementById('car-registration-input')
    if (input.value !== ''){
        axios.post(`/signUp/${input.value}/`)
            .then(response => {
                console.log(response)
            })
            .catch(err => {
                console.log(err.response.data)
                displayError(err.response.data)
            })
    }
    input.value = ''
        
}

function signOut(student_id){
    axios.post(`/signOut/${student_id}/`)
    .then(response => {
        console.log(response)
    })
    .catch(err => {
        console.log(err.response.data)
    })
}
