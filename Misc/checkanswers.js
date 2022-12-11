function checkAnswers()
{
    document.getElementById("results").innerHTML = "";
    for(var property in answers)
    {
        if(answers.hasOwnProperty(property))
        {
            var spanResult = document.createElement("span");
            if(document.getElementById(property).value.toUpperCase() == answers[property].toUpperCase())
            {
                spanResult.innerHTML = property + " Correct - You answered:" + document.getElementById(property).value + " and the correct answer is:" + answers[property];
                spanResult.style.backgroundColor = "#2ecc71";
                
            }
            else
            {
                spanResult.innerHTML = property + " Incorrect - You answered:" + document.getElementById(property).value + " and the correct answer is:" + answers[property];
                spanResult.style.backgroundColor = "#e74c3c";
            }
            document.getElementById("results").appendChild(spanResult);
            document.getElementById("results").appendChild(document.createElement("br"));
        }
    }
}