function random255() {
    return Math.floor(Math.random()*255)
}

function changeColor(r,g,b) {
    document.querySelector(
        "body"
      ).style = `background-color: rgb(${r}, ${g}, ${b})`;
};

function generateLabels(R) {
    let labels = [];
    for (let i = 0; i<1000; i++){
        labels.push(R*i/1000)
    };
    return labels;
}

function generateData(h) {
    let data = [];
    for (let i = 0; i<1000; i++){
        data.push(h*i*(1000-i)/250000)
    };
    return data;
}