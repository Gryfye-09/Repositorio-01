var mainImg = document.getElementById('mainImg');
var titleArea = document.getElementById('titleArea');
var lifeFill = document.getElementById('lifeFill');
var defFill = document.getElementById('defFill');
var jumpFill = document.getElementById('jumpFill');
var lifeNum = document.getElementById('lifeNum');
var defNum = document.getElementById('defNum');
var jumpNum = document.getElementById('jumpNum');

function updateAll(imgSrc, titleStr, lifeVal, defVal, jumpVal){
  mainImg.setAttribute('src', imgSrc);
  titleArea.innerHTML = titleStr;
  lifeFill.style.width = (lifeVal + '%');
  defFill.style.width = (defVal + '%');
  jumpFill.style.width = (jumpVal + '%');
  lifeNum.innerHTML = (lifeVal + '/100');
  defNum.innerHTML = (defVal + '/100');
  jumpNum.innerHTML = (jumpVal + '/100');
}
