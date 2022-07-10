let butPlay = document.querySelector('.play')
let butPause = document.querySelector('.pause')
let butNext = document.querySelector('.next')
let butPrev = document.querySelector('.prev')
let audio = document.querySelector('.audio')
// let  audioSrc = document.getElementById('audio').src
const progress = document.querySelector('.progress')
const progressBar = document.querySelector('.progress-bar')
let namesong = document.querySelector('.name-song')
let songs = document.querySelectorAll('.sound')
let index = 0


function loadSong(index=0){
    audio.src = `${songs[index].innerHTML}`
    // audio.src = `${audioSrc}.substring (${audioSrc}.lastIndexOf('/')+1)`
    // (`${songs[index].innerHTML}`)
    // audio.src = `media/${allsong[index].innerHTML}`
    

    // console.log(audio.src)
    path = (songs[index].innerHTML).split('/')
    path = path[path.length -1] 
    namesong.innerHTML = path

}
loadSong()
butPlay.onclick = function(){
    document.querySelector('audio').play()
}

butPause.onclick = function(){
    document.querySelector('audio').pause()
}
butNext.onclick = function(){
    
    if (index > songs.length -1){
        loadSong(index = 0)
    } else{
        loadSong(index++)
    }
    document.querySelector('audio').play()

}
butPrev.onclick = function(){
    loadSong(index--)
    document.querySelector('audio').play()
}
function updateProgress(e){
    const {duration, currentTime} = e.srcElement
    const progrtessPersent = (currentTime/duration) * 100
    progress.style.width = `${progrtessPersent}%`
}
audio.addEventListener('timeupdate', updateProgress)





function setProgress(e){
    const width = this.clientWidth
    const clickX = e.offsetX
    // console.log(clickX)
    const duration = audio.duration
        // console.log(duration)
    let time = (clickX/width)*duration
    console.log(time)
    audio.currentTime = time
    console.log(audio.currentTime)
}
progressBar.addEventListener('click', setProgress)


