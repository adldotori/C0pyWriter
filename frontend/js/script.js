function uploadFile() {
  String.prototype.replaceAll = function (org, dest) {
    return this.split(org).join(dest);
  }

function uploadFile() {
  $('.lds-hourglass').show();
  event.preventDefault();
  var formData = new FormData();
  formData.append("tab2exkey", "740.3FC485BF078F7CF4");
  formData.append("fileName", "sample");
  formData.append("recognitionMethod", "auto");
  formData.append("outputFormat", "TXT");
  formData.append("file", jQuery("#pdf").get(0).files[0]);

  const reader = new FileReader();
  reader.addEventListener('loadend', (e) => {
    const text = e.srcElement.result.replaceAll('\n', '');
    $.post(API_URL, {
      'text': text
    }, function (data) {
      console.log(data);
    });
  });

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    var a;
    if (xhttp.readyState === 4 && xhttp.status === 200) {
      a = document.createElement("a");
      a.href = window.URL.createObjectURL(xhttp.response);
      reader.readAsText(xhttp.response);
      // console.log(xhttp.responseText);
      a.download = "sample.txt";
      a.style.display = "none";
      document.body.appendChild(a);
      a.click();
      $('.lds-hourglass').hide();
    }
  };
  xhttp.open("POST", "http://api2.pdfextractoronline.com:8089/tab2ex2/api");
  xhttp.responseType = "blob";
  xhttp.send(formData);
};

$(function () {
  $("pdf").click(function () {
    console.log("pdf");
    alert("hello");
    // $.get(API_URL, {}, function (data) {
    //     console.log(data);
    // });
  });
});

$(function () {
  $("summary").click(function () {
    console.log("summary");
    // $.get(API_URL, {}, function (data) {
    //     console.log(data);
    // });
  });
});

$(function () {
  $("complete").click(function () {
    console.log("complete");
    // $.get(API_URL, {}, function (data) {
    //     console.log(data);
    // });
  });
});