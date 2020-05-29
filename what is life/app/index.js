// URLs, keys
const url = "https://gateway.marvel.com:443/v1/public/characters";
const publicKey = "8fe7ec95adf43ed313f550475db00659";
const privateKey = "e8d26a15accc6c93acf5311259da0f59e1b3afab";

// generate key using public and private key
const key = marvelKey(privateKey, publicKey);

// generate special URL using provided key
const fullURL = `${url}?${key}`;

// renders content with given character data
function renderCharacters (characterData) {

    // fetches content div
    const content = document.getElementById("content");

    // deletes all before data to be replaced with new search results
    content.textContent = "";

    // checks if anything is returned
    if (characterData.length > 0) {

        console.log(characterData);

        // loops through every character available
        for (let i = 0; i < characterData.length; i++) {
            let character = characterData[i];

            // pull out character data: name, image, comics, ...
            const characterId = character.id;
            const characterName = character.name;
            const characterAvailableComics = character.comics.available;
            const characterImgSource = character.thumbnail.path + "." + character.thumbnail.extension;

            // create HTML content to append
            let characterHTMLContent = `
                <div charid="${characterName}" class='character' style='width:300px;'>
                    <img src="${characterImgSource}" style='width:300px; height:300px; border: 3px #000000 solid; border-radius: 10%;'/>
                    <div style='text-align:center; font-weight:900;font-size:24px'>${characterName}</div>
                    <div style='text-align:center;'>${characterAvailableComics} available comics</div>
                </div>
            `;

            content.insertAdjacentHTML("beforeend", characterHTMLContent);

        }

        let ballContainerElement = document.getElementById('content');
        let ballElements = ballContainerElement.getElementsByClassName('character');

        for (let i = 0; i < ballElements.length; i++) {
            ballElements[i].addEventListener("click", function (e) {
                displayCharacterInfo(ballElements[i].getAttribute('charid'));
            })
        }

    } else {
        // create HTML content to append
		let characterHTMLContent = `
			<div>Nothing was found :(</div>
		`;

		content.insertAdjacentHTML("beforeend", characterHTMLContent);
    }
}

function displayCharacterInfo (name) {
    let searchURL = `${url}?${key}&nameStartsWith=${name}`;

    // request data & handle response data
    sendGetRequest(searchURL, function (responseData) {
        let characterData = responseData.data.results;
        
        // fetches content div
        const content = document.getElementById("content");

        // deletes all before data to be replaced with new search results
        content.textContent = "";

        // loops through every character available
        for (let i = 0; i < characterData.length; i++) {
            let character = characterData[i];

            console.log(character);

            // pull out character data: name, image, comics, ...
            const characterId = character.id;
            const characterName = character.name;
            const characterAvailableComics = character.comics.available;
            const characterImgSource = character.thumbnail.path + "." + character.thumbnail.extension;

            let comics = "<div>";
            let series = "<div>";
            let stories = "<div>";

            for (let j = 0; j < character.comics.items.length; j++) {
                comics += `<div style='font-size:14px;margin:4px;padding-left:8px;padding-right:8px;display:inline-block;background-color:#b3b3b3;'>${character.comics.items[j].name}</div>`;
            }

            for (let j = 0; j < character.series.items.length; j++) {
                series += `<div style='font-size:14px;margin:4px;padding-left:8px;padding-right:8px;display:inline-block;background-color:#b3b3b3;'>${character.series.items[j].name}</div>`;
            }

            for (let j = 0; j < character.stories.items.length; j++) {
                stories += `<div style='font-size:14px;margin:4px;padding-left:8px;padding-right:8px;display:inline-block;background-color:#b3b3b3;'>${character.stories.items[j].name}</div>`;
            }

            comics += "</div>";
            series += "</div>";
            stories += "</div>";

            // create HTML content to append
            let characterHTMLContent = [`
                <div charid="${characterName}" class='character' style='width:300px;'>
                    <img src="${characterImgSource}" style='width:300px; height:300px; border: 3px #000000 solid; border-radius: 10%;'/>
                </div>
                <div style='width:900px; padding-left:16px;'>
                    <div style='font-weight:900;font-size:24px'>${characterName}</div>
                    <div style='font-size:18px'><b>${characterAvailableComics}</b> comics | <b>${character.series.available}</b> series | <b>${character.stories.available}</b> stories</div>
                    <hr>
                    <div style='font-size:15px'><em>${character.description.length < 1 ? "No description for this character." : character.description}</em></div>
                    <hr>
                    <div><b>Comics:</b> ${comics}</div>
                    <div><b>Series:</b> ${series}</div>
                    <div><b>Stories:</b> ${stories}</div>
                </div>
            `];

            for (let j = 0; j < characterHTMLContent.length; j++) {
                content.insertAdjacentHTML("beforeend", characterHTMLContent[j]);
            }

        }
    })
}

// requests data & handle response data function
function fetchCharacters () {
    // request data & handle response data
    sendGetRequest(fullURL, function (responseData) {
        let characterData = responseData.data.results;
        renderCharacters(characterData);
    })
}

function setupEvents () {
    // search function
    let buttonSearch = document.getElementById("btn_search");

    // attach action to button when clicked
    buttonSearch.addEventListener("click", function (e) {
        let searchBar = document.getElementById("search_bar");

        // fetch search value
        const searchString = searchBar.value;

        // checks if search bar is empty
        if (searchString.length > 0) {
            let searchURL = `${url}?${key}&nameStartsWith=${searchString}`;

            // request data & handle response data
            sendGetRequest(searchURL, function (responseData) {
                let characterSearchData = responseData.data.results;
                renderCharacters(characterSearchData);
            })
        } else {
            // request data & handle response data
            sendGetRequest(fullURL, function (responseData) {
                let characterSearchData = responseData.data.results;
                renderCharacters(characterSearchData);
            })
        }

        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera

    })

    // search function
    let buttonBack = document.getElementById("btn_back");

    // attach action to button when clicked
    buttonBack.addEventListener("click", function (e) {
        // request data & handle response data
        sendGetRequest(fullURL, function (responseData) {
            let characterSearchData = responseData.data.results;
            renderCharacters(characterSearchData);
        })

        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
    })
}

fetchCharacters();
setupEvents();