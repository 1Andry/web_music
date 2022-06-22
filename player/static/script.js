let butPlay = document.querySelector('.play')
let butPause = document.querySelector('.pause')
let butNext = document.querySelector('.next')
let butPrev = document.querySelector('.prev')
const audio = document.querySelector('.audio')
// let  audioSrc = document.getElementById('audio').src
const progress = document.querySelector('.progress')
const progressBar = document.querySelector('.progress-bar')
let namesong = document.querySelector('.name-song')
let songs = document.querySelectorAll('.sound')
let index = 0
let allsong = new Array ();

console.log(songs)

function lists() {
    for (let i of songs){
        // (i.substring (i.lastIndexOf('/')+1))
        // console.log(i)
        allsong.push(i)
    }
}
// lists()
console.log(allsong);
// console.log(document.querySelectorAll('.sound'))
// console.log(s.substring (s.lastIndexOf('/')+1))
// console.log(songs.substring (songs.lastIndexOf('/')+1));
// console.log(audio.src);
console.log(`${songs[index].innerHTML}`);
function loadSong(index=0){
    // audio.src = `media/${allsong[index].innerHTML}`
    // audio.src = `${audioSrc}.substring (${audioSrc}.lastIndexOf('/')+1)`
    // (`${songs[index].innerHTML}`)
    // audio.src = `media/${allsong[index].innerHTML}`
    // let a = 'media/Imagine_Dragons_-_Natural_57429538_RO8h7PM.mp3'
    // audio.src = a
    console.log(audio.src)
    path = (songs[index].innerHTML).split('/')
    path = path[path.length -1] 
    namesong.innerHTML = path
    console.log(path)
}
// loadSong()

butPlay.onclick = function(){
    document.querySelector('audio').play()
    console.log('audio.src');
}
butPause.onclick = function(){
    document.querySelector('audio').pause()
    console.log('audio.src')
}
butNext.onclick = function(){
    loadSong(index++)
    document.querySelector('audio').play()
    console.log('audio.src')
}
butPrev.onclick = function(){
    loadSong(index--)
    document.querySelector('audio').play()
}
// function updateProgress(e){
//     const {duration, currentTime} = e.srcElement
//     const progrtessPersent = (currentTime/duration) * 100
//     progress.style.width = `${progrtessPersent}%`
// }
// audio.addEventListener('timeupdate', updateProgress)

// function setProgress(e){
//     const width = this.clientWidth
//     const clickX = e.offsetX
//     const duration = audio.duration
//     let time = (duration/ width)*duration
//     audio.currentTime = time
//     console.log(time)
// }
// progressBar.addEventListener('click', setProgress)



