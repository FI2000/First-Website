  function RandomFact() {
    x = Math.floor(Math.random()*10)
      if (x===0){
        alert("Ducks can fly")
      }
      if (x===1){
        alert("You randomized the number 2")
      }
      if (x===2){
        alert("Most Disney characters wear gloves to keep animation simple")
      }
      if (x===3){
        alert("The first oranges weren’t orange")
      }
      if (x===4){
        alert("Scotland has 421 words for “snow”")
      }
      if (x===5){
        alert("Peanuts aren’t technically nuts")
      }
      if (x===6){
        alert("Armadillo shells are bulletproof")
      }
      if (x===7){
        alert("The longest English word is 189,819 letters long")
      }
      if (x===8){
        alert("Cats have fewer toes on their back paws")
      }
      if (x===9){
        alert("Blue whales eat half a million calories in one mouthful")
      }




    }



  function bgChangeDay(){
  document.body.style.backgroundImage = "url('../static/pictures/bg.png') | initial";
  }



  function bgChangeNight(){
  document.body.style.backgroundImage = "url('../static/pictures/nightmode.jpg')";
  }

  function Time(){
    var d = new Date();
    var n = d.getUTCHours();
    var zone = prompt("Enter a time zone");
    let p;
    if (zone == "MDT") {
      p = n - 6;
      if (p<0){
        var m=p;
        p = 24 + m;
      }
      alert("Current UTC time is " + n + " o'clock and your destination's time is " + p + " o'clock");
      p=0;
    }
    if (zone == "PDT") {
        p = n - 7
        if (p<0){
          p = 24 + p;
        }
        alert("Current UTC time is " + n + " o'clock and your destination's time is " + p + " o'clock");
        p=0;
    }
    if (zone == "MDT") {
        p = n - 6;
        if (p<0){
          p = 24 + p;
        }
      alert("Current UTC time is " + n + " o'clock and your destination's time is " + p + " o'clock");
      p=0;
    }
    if (zone == "CDT") {
        p = n - 5;
        if (p<0){
          p = 24 + p;
        }
      alert("Current UTC time is " + n + " o'clock and your destination's time is " + p + " o'clock");
      p=0;
    }
    if (zone == "EDT") {
        if(n<4){
        p = (24+n) - 4;}
        else{
          p=n-4;
        }
      alert("Current UTC time is " + n + " o'clock and your destination's time is " + p + " o'clock");
      p=0;
    }
    if (zone == "-03") {
        p = n - 3;
        if (p<0){
          p = 24 + p;
        }
      alert("Current UTC time is " + n + " o'clock and your destination's time is " + p + " o'clock");
      p=0;
    }
    if (zone == "BST") {
        p = n + 1
        if (p<0){
          p = 24 + p;
        }
      alert("Current UTC time is " + n + " o'clock and your destination's time is " + p + " o'clock");
      p=0;
    }
    if (zone == "CEST") {
        p = n + 2;
        if (p<0){
          p = 24 + p;
        }
      alert("Current UTC time is " + n + " o'clock and your destination's time is " + p + " o'clock");
      p=0;
    }
    if (zone == "MSK") {
        p = n + 3;
        if (p<0){
          p = 24 + p;
        }
      alert("Current UTC time is " + n + " o'clock and your destination's time is " + p + " o'clock");
      p=0;
    }
    if (zone == "+04") {
        p = n + 4;
        if (p<0){
          p = 24 + p;
        }
      alert("Current UTC time is " + n + " o'clock and your destination's time is " + p + " o'clock");
      p=0;
    }
    if (zone == "IST") {
        p = n + 5;
        if (p<0){
          p = 24 + p;
        }
      alert("Current UTC time is " + n + " o'clock and your destination's time is " + p + " o'clock");
      p=0;
    }
    if (zone == "+08") {
        p = n + 8;
        if (p<0){
          p = 24 + p;
        }
      alert("Current UTC time is " + n + " o'clock and your destination's time is " + p + " o'clock");
      p=0;
    }
    if (zone == "CST") {
        p = n + 8;
        if (p<0){
          p = 24 + p;
        }
      alert("Current UTC time is " + n + " o'clock and your destination's time is " + p + " o'clock");
      p=0;
    }
    if (zone == "JST") {
        p = n + 9;
        if (p<0){
          p = 24 + p;
        }
      alert("Current UTC time is " + n + " o'clock and your destination's time is " + p + " o'clock");
      p=0;
    }
    if (zone == "AEST") {
        p = n + 10;
        if (p<0){
          p = 24 + p;
        }
      alert("Current UTC time is " + n + " o'clock and your destination's time is " + p + " o'clock");
      p=0;
    }
    if (zone == "NZST") {
        p = n + 12;
        if (p<0){
          p = 24 + p;
        }
      alert("Current UTC time is " + n + " o'clock and your destination's time is " + p + " o'clock");
      p=0;
    }



  }