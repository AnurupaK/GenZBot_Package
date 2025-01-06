def getStyle():
    return """
body{
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    background: radial-gradient(pink,rgb(100, 1, 100));
}

.mobile{
    border: 1px solid black;
    width: 400px;
    min-height: 50px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-direction: column;
    border-radius: 13px;
    background: radial-gradient(rgb(209, 206, 206),rgb(35, 34, 34));
    box-shadow: 1px 1px 8px 4px rgb(37, 37, 37);
}

.mobile_heading{
    width: 100%;
    height: 62px;
    display: flex;
    justify-content: center;
    font-family: "Rubik", sans-serif;
    font-size: 1.5rem;
    color: white;
    box-sizing: border-box;
}

p{
    transform: translateY(-17px);
  }

.mobile_screen{
    border: 1px solid rgb(211, 208, 208);
    width: 380px;
    height: 480px;
    border-radius: 11px;
    background-color: white;
    box-shadow: 1px 1px 6px 2px rgb(179, 181, 179) inset;
    padding: 4px 9px;
    box-sizing: border-box;
    overflow: scroll;
    font-family:  "Lobster Two", sans-serif;
    position: relative;
    background: linear-gradient(to bottom, orange, purple);

}

.text_box{
    width: 250px;
    min-height: 60px;
    padding: 5px;
    box-sizing: border-box;
    border: 1px solid white;
    border-radius: 13px;
    display: flex;
    justify-content: flex-start;
    color: white;
}
.user{
    transform: translateX(108px);
    margin:13px 0px;
    background-color: rgb(8, 115, 115);
}

.AI{
    margin: 13px 0px;
    background-color: rgb(45, 101, 233);
}

.mobile_buttons{
    width: 380px;
    height: 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 2px;
    box-sizing: border-box;
    margin-bottom: 7px;

}

.text_area{
   width: 280px;
   height: 50px;
   border-radius: 13px;
   padding: 13px;
   box-sizing: border-box;
   font-size: 1.03rem;
   background-color: rgb(74, 74, 74);
   color: white;
   font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}


.exchange{
    font-size: 1.3rem;
    border-radius: 30px;
    background-color: black;
}

.exchange:hover{
    transform: scale(1.13);
    background-color: rgb(134, 240, 235);
}

.mobile_screen::-webkit-scrollbar {
    display: none;
}

.mobile_screen {
    scrollbar-width: none;
}
"""
