document.querySelectorAll(".drop-area__input").forEach((inputElement) => {
    const dropAreaElement = inputElement.closest(".drop-area");
    let containerUpload = inputElement.closest(".container-upload");
  
    dropAreaElement.addEventListener("click", (e) => {
      inputElement.click();
    });
  
    inputElement.addEventListener("change", (e) => {
      if (inputElement.files.length) {
        updateThumbnail(dropAreaElement, inputElement.files[0]);
      }
    });
  
    dropAreaElement.addEventListener("dragover", (e) => {
      e.preventDefault();
      dropAreaElement.classList.add("drop-area--over");
    });
  
    ["dragleave", "dragend"].forEach((type) => {
      dropAreaElement.addEventListener(type, (e) => {
        dropAreaElement.classList.remove("drop-area--over");
      });
    });
  
    dropAreaElement.addEventListener("drop", (e) => {
        e.preventDefault();
        console.log(e.dataTransfer.files)
        if (e.dataTransfer.files.length > 1) {
            newDivElement = document.createElement("div");
            console.log(inputElement.files.length);
            
            for (let index = 0; index < e.dataTransfer.files.length; index++) {
                textNode = document.createTextNode('this is picture ${index}.');
                newDivElement.appendChild(textNode);
                containerUpload.appendChild(newDivElement);
            }
        }else{
            console.log(inputElement.files);
            inputElement.files = e.dataTransfer.files;
            console.log(inputElement.files.length);
            updateThumbnail(dropAreaElement, e.dataTransfer.files[0]);
        }
            //     inputElement.files = e.dataTransfer.files;
            //     console.log(inputElement.files.length);
            //     updateThumbnail(dropAreaElement, e.dataTransfer.files[0]);
            //   }
    //   if (e.dataTransfer.files.length) {
    //     inputElement.files = e.dataTransfer.files;
    //     console.log(inputElement.files.length);
    //     updateThumbnail(dropAreaElement, e.dataTransfer.files[0]);
    //   }
  
      dropAreaElement.classList.remove("drop-area--over");
    });
  });
  
  /**
   * Updates the thumbnail on a drop Area element.
   *
   * @param {HTMLElement} dropAreaElement
   * @param {File} file
   */
  function updateThumbnail(dropAreaElement, file) {
    console.log(dropAreaElement);
    console.log(file);
    let thumbnailElement = dropAreaElement.querySelector(".drop-area__thumb");
  
    // First time - remove the prompt class
    if (dropAreaElement.querySelector(".drop-area__prompt")) {
      dropAreaElement.querySelector(".drop-area__prompt").remove();
    }
  
    // First time - there is no thumbnail element, so lets create it
    if (!thumbnailElement) {
      thumbnailElement = document.createElement("div");
      thumbnailElement.classList.add("drop-area__thumb");
      dropAreaElement.appendChild(thumbnailElement);
    }

  
    thumbnailElement.dataset.label = file.name;
  
    // Show thumbnail for image files
    if (file.type.startsWith("image/")) {
      const reader = new FileReader();
  
      reader.readAsDataURL(file);
      reader.onload = () => {
        thumbnailElement.style.backgroundImage = `url('${reader.result}')`;
      };
    } else {
      thumbnailElement.style.backgroundImage = null;
    }
  }
  