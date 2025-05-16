document.getElementById('predictButton').addEventListener('click', async function() {  
    const inputText = document.getElementById('inputText').value;  
    const predictionsList = document.getElementById('predictionsList');  
    predictionsList.innerHTML = ''; // Limpiar predicciones anteriores  

    // Hacer llamada a la API  
    const response = await fetch('/predict', {  
        method: 'POST',  
        headers: {  
            'Content-Type': 'application/json'  
        },  
        body: JSON.stringify({ texto: inputText })
    });  

    const result = await response.json();  
    const listItem = document.createElement('li');  
    listItem.textContent = `Predicción: ${result.prediction}`;  
    predictionsList.appendChild(listItem);  
});