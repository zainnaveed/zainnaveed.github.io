function onClickedPredictCrop() {
    console.log("Crop Predict button clicked");
    var n1 = document.getElementById("uiN");
    var p1 = document.getElementById("uiP");
    var k1 = document.getElementById("uiK");
    var temperature1 = document.getElementById("uiTemperature");
    var humidity1 = document.getElementById("uiHumidity");
    var ph1 = document.getElementById("uiPh");
    var rainfall1 = document.getElementById("uiRainfall");
    var preCrop = document.getElementById("uiPredictCrop");
  
     var url = "http://127.0.0.1:5000/get_crop_name"; //Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
    $.post(url, {
        n: parseFloat(n1.value),
        p: parseFloat(p1.value),
        k: parseFloat(k1.value),
        temperature: parseFloat(temperature1.value),
        humidity: parseFloat(humidity1.value),
        ph: parseFloat(ph1.value),
        rainfall: parseFloat(rainfall1.value)
    },function(data, status) {
        console.log(data.crop_name);
        preCrop.innerHTML = "<h2>" + data.crop_name.toString() ;
        console.log(status);
    });
  }