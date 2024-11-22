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