<template>
  <router-view/>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');
::-webkit-scrollbar { height: 6px; width: 5px; background: #17212B;}
::-webkit-scrollbar-thumb { background: #83838370; -webkit-border-radius: 5px; -webkit-box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.75); }
::-webkit-scrollbar-corner { background: #17212B; }
::selection { background: rgba(29, 149, 219, 0.623); color: rgb(255, 255, 255); }
.unselectable {
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none;   /* Chrome/Safari/Opera */
  -khtml-user-select: none;    /* Konqueror */
  -moz-user-select: none;      /* Firefox */
  -ms-user-select: none;       /* Internet Explorer/Edge */
  user-select: none;           /* Non-prefixed version, currently
                                  not supported by any browser */
}
html, body { min-height: 100%; }

body { background: #17212B; margin: 0; padding-bottom: 25px; }
</style>
