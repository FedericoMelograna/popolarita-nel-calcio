function Method() {
          document.getElementById("method").style.display = "block";
          document.getElementById("article").style.display = "none";
          document.getElementById("article_a").setAttribute("class", "clicked");
          document.getElementById("method_a").setAttribute("class", "not_clicked");
      };
      
function Article() {
  document.getElementById("method").style.display = "none";
  document.getElementById("article").style.display = "block";
  document.getElementById("article_a").setAttribute("class", "not_clicked");
  document.getElementById("method_a").setAttribute("class", "clicked");
};