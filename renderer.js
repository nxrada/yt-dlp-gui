const youtubedl = require('youtube-dl-exec')
const urlInput = document.querySelector('#url')
const downloadButton = document.querySelector('#download')

downloadButton.addEventListener('click', () => {
    const url = urlInput.value
    youtubedl(url, {
        dumpSingleJson: true,
        noWarnings: true,
        noCallHome: true,
        noCheckCertificate: true,
        preferFreeFormats: true,
        youtubeSkipDashManifest: true
    }).then(output => console.log(output))
})
