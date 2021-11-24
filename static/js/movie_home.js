let xPos = 0;
console.log("hey")
let movies = []
const URL = 'http://127.0.0.1:8000/movie/randoms/'
axios.get(URL)
.then(function (response) {
  console.log(response.data.data)
  movies = response.data.data
  console.log(movies)
  const images = document.querySelectorAll('.imga')
  let count = 0

  images.forEach(function (image) {
  console.log(movies[count])
  image.setAttribute('href',`http://127.0.0.1:8000/movie/${movies[count].pk}/`)
  count+=1
})
})
.catch((err) => {
  if (err.response.status ===401){
    window.location.href = '/user/login'
  }
})
gsap.timeline()
    .set('.ringa', { rotationY:180, cursor:'grab' })
    .set('.imga',  {
      rotateY: (i)=> i*-36,
      transformOrigin: '50% 50% 500px',
      z: -500,
      backgroundImage:(i)=>`url(${movies[i].posterpath})`,
      backgroundPosition:(i)=>getBgPos(i),
      backfaceVisibility:'hidden'
    })    
    .from('.imga', {
      duration:1.5,
      y:200,
      opacity:0,
      stagger:0.1,
      ease:'expo'
    })
    .add(()=>{
      $('.imga').on('mouseenter', (e)=>{
        let current = e.currentTarget;
        gsap.to('.imga', {opacity:(i,t)=>(t==current)? 1:0.5, ease:'power3'})
      })
      $('.imga').on('mouseleave', (e)=>{
        gsap.to('.imga', {opacity:1, ease:'power2.inOut'})
      })
    }, '-=0.5')

$(window).on('mousedown touchstart', dragStart);
$(window).on('mouseup touchend', dragEnd);
      

function dragStart(e){ 
  if (e.touches) e.clientX = e.touches[0].clientX;
  xPos = Math.round(e.clientX);
  gsap.set('.ringa', {cursor:'grabbing'})
  $(window).on('mousemove touchmove', drag);
}


function drag(e){
  if (e.touches) e.clientX = e.touches[0].clientX;    

  gsap.to('.ringa', {
    rotationY: '-=' +( (Math.round(e.clientX)-xPos)%360 ),
    onUpdate:()=>{ gsap.set('.imga', { backgroundPosition:(i)=>getBgPos(i) }) }
  });
  
  xPos = Math.round(e.clientX);
}


function dragEnd(e){
  $(window).off('mousemove touchmove', drag);
  gsap.set('.ringa', {cursor:'grab'});
}


function getBgPos(i){
  return ( 100-gsap.utils.wrap(0,360,gsap.getProperty('.ring', 'rotationY')-180-i*36)/360*500 )+'px 0px';
}

