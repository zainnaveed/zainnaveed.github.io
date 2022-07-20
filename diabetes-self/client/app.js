function onClickedPredictDiabetes() {
    console.log("Diabetes Predict button clicked");
    var pregnancies1 = document.getElementById("uiP");
    var glucose1= document.getElementById("uiG");
    var bloodpressure1 = document.getElementById("uiBL");
    var skinthickness1 = document.getElementById("uiS");
    var insulin1 = document.getElementById("uiI");
    var bmi1 = document.getElementById("uiBM");
    var diabetespedigreefunction1 = document.getElementById("uiD");
    var age1 = document.getElementById("uiA");
    var preDiabetes = document.getElementById("uiPredictDiabetes");
  
     var url = "http://127.0.0.1:5000/get_diabetes"; //Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
    $.post(url, {
        pregnancies: parseFloat(pregnancies1.value),
        glucose: parseFloat(glucose1.value),
        bloodpressure: parseFloat(bloodpressure1.value),
        skinthickness: parseFloat(skinthickness1.value),
        insulin: parseFloat(insulin1.value),
        bmi: parseFloat( bmi1.value),
        diabetespedigreefunction: parseFloat(diabetespedigreefunction1.value),
        age: parseFloat(age1.value)
    },function(data, status) {
        console.log(data.diabetes);
        preDiabetes.innerHTML = "<h2>" + data.diabetes ;
        console.log(status);
    });
  }