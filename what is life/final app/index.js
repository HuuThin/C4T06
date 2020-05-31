// define english words and their translations
const englishWords = ["architecture", "interview", "experiment", "reservation", "champion", "reasonable", "recruitment", "satisfaction", "repository", "surpression"];
const vietnameseTranslations = ["kiến trúc", "phỏng vấn", "thí nghiệm", "khu bảo tồn", "nhà vô địch", "hợp lý", "sự tuyển dụng", "sự mãn nguyện", "kho tàng chứa", "sự đàn áp"];

let index = 0;
let cardFace = 0;

function updateFlashcardIndex () {
	// get current flashcard index
	let flashcardIndex = document.getElementById('index');
	flashcardIndex.textContent = `${index + 1} / ${englishWords.length}`;
	
	let buttonBack = document.getElementById("buttonBack");
	if (index < 1) { buttonBack.classList.add('disabled'); } else { buttonBack.classList.remove('disabled'); }
	
	let buttonForw = document.getElementById("buttonForw");
	if (index >= englishWords.length - 1) { buttonForw.classList.add('disabled'); } else { buttonForw.classList.remove('disabled'); }
}

function updateFlashcard (cardFace) {
	let card = document.getElementById("card");
	
	if (cardFace === 0) {
		card.textContent = englishWords[index];
		card.classList.add('faceFront');
		card.classList.remove('faceBack');
	} else {
		card.textContent = vietnameseTranslations[index];
		card.classList.add('faceBack');
		card.classList.remove('faceFront');
	}
}

function setupFlashcard () {
	// flip the flashcard if clicked
	let card = document.getElementById("card");
	card.addEventListener('click', function () {
		card.classList.toggle('faceBack');
		card.classList.toggle('faceFront');
		cardFace = 1 - cardFace;
		updateFlashcard(cardFace);
	});
}

function setupButtons () {
	
	// back button
	let buttonBack = document.getElementById("buttonBack");
	buttonBack.addEventListener('click', function () {
		index = (index < 1) ? 0 : index - 1;
		updateFlashcardIndex();
		updateFlashcard(0);
		
		if (index < 1) { buttonBack.classList.add('disabled'); } else { buttonBack.classList.remove('disabled'); }
	});
	
	// forward button
	let buttonForw = document.getElementById("buttonForw");
	buttonForw.addEventListener('click', function () {
		index = (index >= englishWords.length - 1) ? englishWords.length - 1 : index + 1;
		updateFlashcardIndex();
		updateFlashcard(0);
		
		if (index >= englishWords.length - 1) { buttonForw.classList.add('disabled'); } else { buttonForw.classList.remove('disabled'); }
	});
}

setupFlashcard();
updateFlashcardIndex();
setupButtons();
updateFlashcard(0);