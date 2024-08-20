window.onload = () =>{
    const player = {
        element : document.getElementById('img'),
        topPosition: 0,
        LeftPosition: 0,
        step: 25,
        move : function(direction){
            switch(direction){
                case 'KeyW':
                    this.topPosition = this.topPosition - this.step;
                    this.element.style.top = this.topPosition + "px";
                    break;
                case 'KeyS':
                    this.topPosition = this.topPosition + this.step;
                    this.element.style.top = this.topPosition + "px";
                    break;
                case 'KeyA':
                    this.LeftPosition = this.LeftPosition - this.step;
                    this.element.style.left = this.LeftPosition + "px";
                    break;
                case 'KeyD':
                    this.LeftPosition = this.LeftPosition + this.step;
                    this.element.style.left = this.LeftPosition + "px";
                    break;

                default:
                    break;
            }
        }
    };
    onkeydown = (Key) =>{
        console.log(Key.code)
        player.move(Key.code)
    }
}