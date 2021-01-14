window.onload = function () {
  let stopButton = document.getElementById("stop")
  let restartButton = document.getElementById("restart")
  let display = document.getElementById("display")

  let startTime, stopTime

  setTimeout(start, 1000)

  function start() {
    restartButton.onclick = null
    stopButton.onclick = stop
    startTime = new Date()
    function stop() {
      stopTime = new Date()
      stopButton.onclick = null
      display.innerHTML = (stopTime - startTime).toString() + "ms"
      restartButton.onclick = start
    }
  }
}
