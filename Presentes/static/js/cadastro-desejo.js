function previewImage(input) {
    var preview = document.getElementById('foto');
    var file = input.files[0];
    var reader = new FileReader();

    reader.onloadend = function () {
      preview.src = reader.result;
    };

    if (file) {
      reader.readAsDataURL(file);
    } else {
      preview.src = '';
    }
  }

  // Adicione o seguinte trecho para chamar a função quando um arquivo é selecionado
  document.getElementById('id_foto').addEventListener('change', function () {
    previewImage(this);
  });