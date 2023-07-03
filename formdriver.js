var driverObject = {
    "Matt": {"Leaving":{"Work":0,"Home":1}, "Arriving":{"Work":0,"Home":1}},
    "Evan": {"Leaving":{"Work":0,"Home":1}, "Arriving":{"Work":0,"Home":1}}
  }
  window.onload = function() {
    startTime()
    var driverSel = document.getElementById("driver");
    var stageSel = document.getElementById("stage");
    var directionSel = document.getElementById("direction");
    var submitBtn = document.getElementById("submit");

    checkDisabled();

    

    for (var x in driverObject) {
      driverSel.options[driverSel.options.length] = new Option(x, x);
    }
    driverSel.onchange = function() {
      
      //empty Chapters- and Topics- dropdowns
      stageSel.length = 1;
      directionSel.length = 1;
      //display correct values
      for (var y in driverObject[this.value]) {
        stageSel.options[stageSel.options.length] = new Option(y, y);
      }
      checkDisabled();
    }

    stageSel.onchange = function() {
      directionSel.length = 1;

      for (var z in driverObject[driverSel.value][this.value]) {
        directionSel.options[directionSel.options.length] = new Option(z, z);
      }
      checkDisabled();
    }

    directionSel.onchange = function() {
      checkDisabled();
    }
  }

  function checkDisabled() {
    var driverSel = document.getElementById("driver");
    var stageSel = document.getElementById("stage");
    var directionSel = document.getElementById("direction");
    var submitBtn = document.getElementById("submit");
    let dIsSel = (driverSel.selectedIndex > 0);
    let sIsSel = (stageSel.selectedIndex > 0);
    let rIsSel = (directionSel.selectedIndex > 0);

    stageSel.disabled = (!dIsSel);
    directionSel.disabled = (!dIsSel || !sIsSel);
    submitBtn.disabled = (!dIsSel ||!sIsSel || !rIsSel);

    if (dIsSel) {
      driverSel.classList.add("is-selected");
    }
    else {
      driverSel.classList.remove("is-selected");
      stageSel.classList.remove("is-selected");
      directionSel.classList.remove("is-selected");
    }

    if (sIsSel) {
      stageSel.classList.add("is-selected");
    }
    else {
      stageSel.classList.remove("is-selected");
      directionSel.classList.remove("is-selected");
    }

    if (rIsSel) {
      directionSel.classList.add("is-selected");
    }
    else {
      directionSel.classList.remove("is-selected");
    }

  }

  function startTime() {
    console.log("clock started");
    const today = new Date();
    let h = ((today.getHours() - 1) % 12) + 1;
    let half = " AM"
    // if (today.getHours() == 12) {
    //   h += 12;
    // }
    if (today.getHours() >= 12) {
      half = " PM";
    }
    let m = today.getMinutes();
    let s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('clock-digital').innerHTML =  h + ":" + m + half;
    setTimeout(startTime, 1000);
  }

  function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
  }