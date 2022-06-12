let butPlay = document.querySelector('.play')
let butPause = document.querySelector('.pause')
let butNext = document.querySelector('.next')
let butPrev = document.querySelector('.prev')
const audio = document.querySelector('.audio')
const progress = document.querySelector('.progress')
const progressBar = document.querySelector('.progress-bar')
let namesong = document.querySelector('.name-song')
let songs = document.getElementsByClassName('sound');
let index = 0

// function shortName(){
//     return songs.innerHTML = songs.replace('uploads/', '')
// }
// shortName()

function newName(){
    return document.getElementsByClassName('sound').innerText = 'newText'
    console.log('+++')
}
newName()

function loadSong(index=0){
    audio.src = `media/${songs[index].innerHTML}`
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
    loadSong(index++)
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
    const duration = audio.duration
    let time = (duration/ width)*duration
    audio.currentTime = time
    console.log(time)
}
progressBar.addEventListener('click', setProgress)


// console.log(sounds[0])


    

// for (let i=0; i<sounds.length; i++){
//     console.log(sounds[i])
// }


// let player = document.getElementById('current_song')
// console.log(player)

// function loadSong(song){
//     audio.src = song
// }
// loadSong(sounds[soundIndex])

// function nextSong (){
//     soundIndex++
// }

// for(let i=0; i<sound.length; i++){
//     console.log(sound[i])
// }