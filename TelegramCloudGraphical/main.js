const electron = require('electron')
const url = require('url')
const path = require('path')

const { app, BrowserWindow } = electron

let mainWindow;

app.on('ready', function() {
    mainWindow = new BrowserWindow({
        autoHideMenuBar: true,
        frame: true,
        width: 1400,
        height: 600,

    })
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'html/mainWindow.html'),
        protocol: "file:",
        slashes: true
    }))
})
