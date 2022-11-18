function showBtn(group, btn_id){
    console.log('hovering')
    console.log("btn_"+group+"_"+btn_id)
    const btn = document.getElementById("btn_"+group+"_"+btn_id)
    btn.style.opacity = 1
}
    
function hideBtn(group, btn_id){
    console.log('leaving')
    console.log("btn_"+group+"_"+btn_id)
    const btn = document.getElementById("btn_"+group+"_"+btn_id)
    btn.style.opacity = 0
}
