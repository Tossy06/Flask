document.addEventListener('DOMContentLoaded', function(){
    var i = 0;
    const bienvenida = document.querySelector('.txt');
    const contenido = bienvenida.textContent;
    const principal = document.querySelector('.principal');
    principal.style.display = 'none';

    bienvenida.textContent = '';
    function Typewrite(){
        if(i < contenido.length){
            bienvenida.textContent += contenido.charAt(i);
            i++;
            setTimeout(Typewrite,100)
        }else{
            setTimeout(borrar, 1000)
        }
    }
    function borrar(){
        if(i >=0){
            bienvenida.textContent = contenido.substring(0, i);
            i--;
            setTimeout(borrar, 100)
        }
        else{
            controlvistas()
        }
    }
    function controlvistas(){
        bienvenida.style.display= 'none'
        principal.style.display = 'block'
    }

    Typewrite();
    
});