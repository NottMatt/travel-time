var driverObject = {
    "Matt": {"Leaving":0, "Arriving":1},
    "Evan": {"Leaving":0, "Arriving":1}
  }
  window.onload = function() {
    startTime()
    var driverSel = document.getElementById("driver");
    var stageSel = document.getElementById("stage");
    var submitBtn = document.getElementById("submit");

    checkDisabled();

    

    for (var x in driverObject) {
      driverSel.options[driverSel.options.length] = new Option(x, x);
    }
    driverSel.onchange = function() {
      checkDisabled();
      //empty Chapters- and Topics- dropdowns
      stageSel.length = 1;
      //display correct values
      for (var y in driverObject[this.value]) {
        stageSel.options[stageSel.options.length] = new Option(y, y);
      }

      if(driverSel.selectedIndex > 0) {
        driverSel.classList.add("is-selected");
      }
      else {
        driverSel.classList.remove("is-selected");
        stageSel.classList.remove("is-selected");
      }
    }
    stageSel.onchange = function() {
      checkDisabled();
      if(stageSel.selectedIndex > 0) {
        stageSel.classList.add("is-selected");
      }
      else {
        stageSel.classList.remove("is-selected");
      }
    }
  }

  function checkDisabled() {
    var driverSel = document.getElementById("driver");
    var stageSel = document.getElementById("stage");
    var submitBtn = document.getElementById("submit");
    let dIsSel = (driverSel.selectedIndex > 0);
    let sIsSel = (stageSel.selectedIndex > 0);

    stageSel.disabled = (!dIsSel);
    submitBtn.disabled = (!dIsSel ||!sIsSel);

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
    document.getElementById('clock').innerHTML =  h + ":" + m + half;
    setTimeout(startTime, 1000);
  }

  function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
  }