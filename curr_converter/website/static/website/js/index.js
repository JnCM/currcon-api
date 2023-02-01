document.addEventListener("DOMContentLoaded", function(e) {
    const todayDate = new Date();
    let copyright = document.getElementById("copyright");
    copyright.textContent = `${todayDate.getFullYear()} | All rights reserved.`;
});

function isValid(amount){
    const exp = /^\d*(\.)?\d*$/;
    if(exp.test(amount.value)){
        return true;
    }
    amount.value = "";
}

async function checkFields(){
    const amount = document.getElementById("amount").value;
    const originCurrency = document.getElementById("ori-currency").value;
    const targetCurrency = document.getElementById("tgt-currency").value;

    if(amount === "" || originCurrency === "" || targetCurrency === ""){
        alert("Please fill all the fields before clicking in the button!");
    }else if(originCurrency === targetCurrency){
        alert("Please select different currencies to convert!");
    }else{
        await makeRequest(amount, originCurrency, targetCurrency);
    }
}

async function makeRequest(amount, originCurrency, targetCurrency){
    const url = `/converter?from=${originCurrency}&to=${targetCurrency}&amount=${parseFloat(amount)}`;
    await axios.get(url).then((response) => {
        if(response.data.message === "success"){
            document.getElementById("result").value = response.data.result;
        }else{
            alert(response.data.message);
        }
    });
}