let url = `ws://${window.location.host}/ws/socket-server/`

const scoket = new WebSocket(url)

scoket.onmessage = function(e){
    let data = JSON.parse(e.data)
    console.log('Data:', data)
    if (data.type === 'message'){
        console.log(data.message)
    } 
    else if (data.type === 'add_student'){
        //window.location.reload();
        const student = data.data
        const list = $(`#list-group-${student.student_class}`)
        add_student_to_list(list, student)
    }
    else if (data.type === 'remove_student'){
        const student = data.data
        remove_student_from_list(student)
    }
}


function add_student_to_list(list, data){
    const n = list.children().length
    const template = `
    <li class="list-group-item" id="student-${data.student_id}"
                                onmouseover="showBtn('${data.student_class}','${n}')" 
                                onmouseout="hideBtn('${data.student_class}','${n}')" >
        <div class="flex-container">
            <div>${data.student_name} (${data.car_id})</div>
            <div class="right-align">
                <button id="btn_${data.student_class}_${n}" class="mark_btn btn btn-sm btn-outline-danger" type="button" onclick="signOut('${data.student_id}')">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check" viewBox="0 0 16 16">
                        <path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.267.267 0 0 1 .02-.022z"/>
                    </svg>
                </button>
            </div>
        </div>
    </li>
    `
    list.append(template);
}

function remove_student_from_list(data){
    const student = document.getElementById(`student-${data.student_id}`)
    console.log(student, `student-${data.student_id}`)
    student.remove()
    const left_count = $(`#left-count-${data.student_class}`)
    const not_left_count = $(`#not-left-count-${data.student_class}`)
    increment(left_count)
    decrement(not_left_count)
}

function increment(count_label){
    count_label.html((parseInt(count_label.html(),10) || 0) + 1);
}

function decrement(count_label){
    count_label.html((parseInt(count_label.html(),10) || 0) - 1);
}