var Image = new Array("images/show1.jpg","images/show2.jpg","images/show3.jpg","images/show4.jpg");
var Image_Number = 0;

var Image_length = Image.length - 1;

function change_image(num){
    Image_Number = Image_Number + num;
    
    if (Image_Number > Image_length){
        Image_Number = 0;
    }
    
    if (Image_Number < 0){
        Image_Number = Image_length;
    }
    
    document.slideshow.src = Image[Image_Number];
    return false;
}

function auto(){
    setInterval("change_image (1)", 5000);
}




