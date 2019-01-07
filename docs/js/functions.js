var toggleClass=function(s,c1,c2){
    if (s.className !== c1){s.className = c1;}
    else {s.className = c2;}
};

function Show(x){
    var e = document.getElementById(x);
    var l = document.getElementsByClassName('graph_bolle');
    for (var i = 0; i < l.length; i++){
        l[i].style.display = 'none';
    }
    e.style.display = 'block';  
    var k = document.getElementsByClassName('clicked1');
    toggleClass(k[0], 'clicked1', 'not_clicked1');
    toggleClass(document.getElementById(x+'_button'), 'not_clicked1', 'clicked1');
};

function Show2(x){
    var e = document.getElementById(x);
    var l = document.getElementsByClassName('graph_boxplot');
    for (var i = 0; i < l.length; i++){
        l[i].style.display = 'none';
    }
    e.style.display = 'block';  
    var k = document.getElementsByClassName('clicked2');
    toggleClass(k[0], 'clicked2', 'not_clicked2');
    toggleClass(document.getElementById(x+'_button2'), 'not_clicked2', 'clicked2');
};