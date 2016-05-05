var Image = new Array("http://purplecresteducation.com/images/slider/sl2.jpg","http://purplecresteducation.com/images/slider/sl1.jpg","https://pbs.twimg.com/media/Cb4-G2EWEAANlMQ.jpg","https://thegarageflower.files.wordpress.com/2015/12/img_2899.jpg?w=1100&h=500&crop=1");
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




