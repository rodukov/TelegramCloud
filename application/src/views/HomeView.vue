<template>
        <div class="mainWindow">

            <!--div class="search-container">
                
            </div-->

            <div class="mainWindow-body">

                <div class="file-storages-and-archives">
                    <!--p class="res about-fsaa">Your Archives</p-->
                    <div class="new-search">
                        <input class="search-files" placeholder="Search Files...">
                    </div>
                    <div class="telegram-items">

                        <div class="telegram-item">
                            <div class="gen-img-c" id="avatar-purple"></div>
                            <div class="text-fsaa-items">
                                <div><p class="res fsaa-name unselectable">Awesome Photos</p></div>
                                <div><p class="res fsaa-description unselectable">My awesome photo</p></div>
                            </div>
                        </div>
                        <div class="telegram-item">
                            <div class="gen-img-c" id="avatar-blue"></div>
                            <div class="text-fsaa-items">
                                <div><p class="res fsaa-name unselectable">Music Archive</p></div>
                                <div><p class="res fsaa-description unselectable">Niztes - River</p></div>
                            </div>
                        </div>
                        <div class="telegram-item">
                            <div class="gen-img-c" id="avatar-orange"></div>
                            <div class="text-fsaa-items">
                                <div><p class="res fsaa-name unselectable">Books Archive</p></div>
                                <div><p class="res fsaa-description unselectable">Rich dad and poor dad</p></div>
                            </div>
                        </div>
                        <div class="telegram-item" style="background: #2B5378">
                            <div class="gen-img-c" id="avatar-green"></div>
                            <div class="text-fsaa-items">
                                <div><p class="res fsaa-name unselectable">My secret diary</p></div>
                                <div><p class="res fsaa-description unselectable" style="color: white;">Dear Diary! Today for the first time...</p></div>
                            </div>
                        </div>
                    </div>
                </div>
    
                <div class="content-viewer">
                    <div class="file-item">
                        <div><p class="res filetext">Lorem Ipsum is simply dummy text of the printing and typesetting industry.
                            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
                            when an unknown printer took a galley of type and scrambled it to make a type specimen book.
                            It has survived not only five centuries, but also the leap into electronic typesetting,
                            remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset
                            sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like
                            Aldus PageMaker including versions of Lorem Ipsum.</p></div>
                            <div class="fileimg-container">
                                <div><img class="res fileimage unselectable" src="https://upload.wikimedia.org/wikipedia/commons/4/4b/La_Tour_Eiffel_vue_de_la_Tour_Saint-Jacques%2C_Paris_ao%C3%BBt_2014_%282%29.jpg"></div>
                                <div><img class="res fileimage unselectable" src="https://upload.wikimedia.org/wikipedia/commons/4/4b/La_Tour_Eiffel_vue_de_la_Tour_Saint-Jacques%2C_Paris_ao%C3%BBt_2014_%282%29.jpg"></div>  
                                <div><img class="res fileimage unselectable" src="https://upload.wikimedia.org/wikipedia/commons/4/4b/La_Tour_Eiffel_vue_de_la_Tour_Saint-Jacques%2C_Paris_ao%C3%BBt_2014_%282%29.jpg"></div>      

                            </div>
                        <p class="res time unselectable">18:31</p>
                
                    </div>

                    <div class="file-item">
                        <div><img class="res fileimage unselectable" src="https://upload.wikimedia.org/wikipedia/commons/4/4b/La_Tour_Eiffel_vue_de_la_Tour_Saint-Jacques%2C_Paris_ao%C3%BBt_2014_%282%29.jpg"></div>
                        <p class="res time unselectable">12:58</p>
                    </div>

                    <div class="file-item">
                        <div><p class="res filetext">Lorem Ipsum is simply dummy text of the printing and typesetting industry.
                            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
                            when an unknown printer took a galley of type and scrambled it to make a type specimen book.
                            It has survived not only five centuries, but also the leap into electronic typesetting,
                            remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset
                            sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like
                            Aldus PageMaker including versions of Lorem Ipsum.</p></div>
                        <p class="res time unselectable">19:19</p>
                    </div>

                </div>

            </div>

        </div>
</template>

<script>
export default {
  name: 'MainWindow',
  data() {
    return {

    }
  },
  mounted() {
    document.title = "Telegram Cloud"




  }
}
</script>

<style scoped>
.time { text-align: right; padding: 5px; color: #879AAC; font-family: 'arial'; font-size: 14px; }
            .res { margin: 0; } /* reset paragraph margin */
            .search-container {
                background: rgb(32, 32, 70);
                padding: 13.5px;
            }
            .mainWindow-body {
                display: flex;
                min-height: 100%;
                
            }
            .file-storages-and-archives {
                min-width: 300px;
                background: #17212B;
            }
            .telegram-item { 
                background-color: #17212B;
                color: white;
                display: flex;
                border-bottom: 1px solid rgb(66, 66, 66);
                padding: 5px; /* You can switch to margin */
                padding-top: 5px;
                padding-bottom: 5px;
                transition: .1s;
                font-family: 'arial';
                font-size: 14px;
            }
            .telegram-item:hover {
                background: #202B36;
            }

            .about-fsaa {
                text-align: left;
                margin: 5px;
                font-size: 16px;
                margin-left: 15px;
                display: inline-block;
                font-family: arial;
            }
            .gen-img {
                background: rgb(89, 0, 255);
                margin: auto;
            }
            .gen-img-c {
                width: 48px;
                height: 48px;
                border-radius: 50%;
            }
            #avatar-blue { background: linear-gradient(160deg, rgb(158, 224, 255), rgb(0, 174, 255)); }
            #avatar-purple { background: linear-gradient(170deg, rgb(211, 170, 255), rgb(119, 0, 255)); }
            #avatar-orange { background: linear-gradient(120deg, #cfa681, #DB863B); }
            #avatar-green { background: linear-gradient(160deg, rgb(166, 230, 169), rgb(55, 207, 62)); }
            #avatar-yellow { background: linear-gradient(160deg, rgb(158, 224, 255), rgb(0, 174, 255)); }

            .text-fsaa-items {
                margin-left: 10px;
            }
            .fsaa-name {              
                margin-bottom: 5px;
                font-weight: 900;
            }
            .fsaa-description { color: #879AAC }
            .search-files {
                width: 260px;
                margin: auto;
                padding: 8px;
                border: none;
                outline: none;
                border-radius: 7px;
                text-align: center;
                transition: .1s;
                display: block;
                margin: auto;
                width: 90%;
                background: #242F3D;
                color: white;
                font-family: 'arial';
                
            }
            .search-files:focus {
                outline: 2px solid rgba(0, 162, 255, 0.514);
                
            }
            .new-search {
                margin-top: 8px;
                margin-bottom: 8px;
            }


            /* Viewer */
            .file-item {
                background: #182533;
                margin: 8px;
                border-radius: 3px;
                color: white;
                font-family: 'Lato', sans-serif;
                text-align: left;
                display: inline-block;
            }
            .filetext {
                padding: 20px;
                padding-bottom: 0;
            }
            .fileimage {
                max-height: 300px;
                max-width: 300px;
                min-width: 1px;
                min-height: 1px;
                border-radius: 5px;
                transition: .3s;
                margin: 20px;
                margin-bottom: 0px;
            }
            .content-viewer {
                background-color: #0E1621;
                padding: 7.5px;
                border-radius: 0px 0px 0px 20px;
                max-height: 555px;
                overflow: auto;
            }
            .fileimg-container {
                display: grid;
                grid-template-columns: 33.3333333333% 33.3333333333% 33.3333333333%;

            }
</style>
