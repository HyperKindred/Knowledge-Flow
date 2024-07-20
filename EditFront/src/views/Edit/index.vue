<template>
  <div class="EditMain" ref="filecont" >
    <OpenAnimation/>
    <img class="background" :src=currentImage />
    <div class="lefttools">
      <div class="lefttop">
        <img :src="misakaImg" alt="Misaka Mikoto">
        <h2 class="username-display">{{ store.username }}</h2>
        <div id="theme-icon">
        <svg t="1721014017349" id="sun-icon" class="sun" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4447" width="200" height="200"><path d="M270.387022 463.499421A226.484357 226.484357 0 1 1 496.871379 689.983778a226.484357 226.484357 0 0 1-226.484357-226.484357z" fill="#FFDA6A" p-id="4448"></path><path d="M496.12978 823.76825a16.31518 16.31518 0 0 1-8.899189-2.966396L444.959444 790.396292a16.611819 16.611819 0 0 1-3.707996-22.989571 16.760139 16.760139 0 0 1 23.137892-3.856315l33.371958 24.176129 36.190035-22.247972a16.463499 16.463499 0 0 1 16.908458 28.329085l-46.127462 27.735805a16.611819 16.611819 0 0 1-8.602549 2.224797z m193.705678-88.10197a16.463499 16.463499 0 0 1-4.746234-32.482039l41.677868-10.382387 6.674391-40.19467a16.463499 16.463499 0 0 1 32.630359 5.339514l-8.454229 51.318655a16.908459 16.908459 0 0 1-12.310545 13.348784l-52.208574 13.052143zM311.471611 733.738123a12.013905 12.013905 0 0 1-3.263036 0l-51.318656-8.45423a16.463499 16.463499 0 0 1-13.348783-12.310544l-13.052144-52.060255a16.463499 16.463499 0 1 1 31.59212-8.30591l10.382387 41.826188 40.49131 6.526072a16.463499 16.463499 0 0 1-1.483198 32.778679z m187.772885-17.650058a251.253766 251.253766 0 1 1 250.660487-251.253766 251.253766 251.253766 0 0 1-251.105446 251.253766z m0-32.926999a218.326767 218.326767 0 1 0-218.771727-218.326767 218.326767 218.326767 0 0 0 218.326768 218.326767z m-312.954809-156.180765a16.01854 16.01854 0 0 1-14.831981-7.86095l-27.735806-46.275782a16.463499 16.463499 0 0 1 0.741599-18.095017l29.663963-42.271148a16.463499 16.463499 0 0 1 26.697567 19.281576L177.983778 465.279258l22.099652 36.783314a16.463499 16.463499 0 0 1-5.636153 22.544612 14.831981 14.831981 0 0 1-8.15759 2.373117z m625.019699 0a14.831981 14.831981 0 0 1-7.71263-2.373117 16.463499 16.463499 0 0 1-5.636153-22.544612l22.099652-36.783314-23.87949-33.520278a16.16686 16.16686 0 0 1 3.707995-22.841251 16.463499 16.463499 0 0 1 22.989571 3.559675l30.405562 42.271148a16.31518 16.31518 0 0 1 0 18.095017L826.141367 519.119351a16.01854 16.01854 0 0 1-14.831981 7.86095zM338.910776 470.173812a16.463499 16.463499 0 0 1-14.831981-17.501738c3.263036-50.577057 19.429896-90.030127 49.242178-117.469293a185.103129 185.103129 0 0 1 118.655852-43.012746 16.463499 16.463499 0 1 1 1.779838 32.926999c-44.495944 2.373117-76.533024 14.090382-98.780997 34.410197s-35.745075 50.577057-38.563152 95.221321a16.611819 16.611819 0 0 1-17.501738 15.42526zM749.015064 294.414832a16.611819 16.611819 0 0 1-14.831982-13.793743l-7.41599-40.639629-41.677868-10.382387a16.463499 16.463499 0 0 1 8.00927-32.03708l52.208574 13.052144a16.760139 16.760139 0 0 1 12.310545 13.348783l8.454229 51.318656a16.908459 16.908459 0 0 1-13.645423 18.984936z m-504.28737-1.928158a12.310545 12.310545 0 0 1-3.263036 0 16.31518 16.31518 0 0 1-12.013905-20.023175l13.052144-52.208574a16.760139 16.760139 0 0 1 13.348783-12.310545l51.318656-8.30591a16.463499 16.463499 0 1 1 5.191194 32.48204l-40.49131 6.674392-10.382387 41.677867a16.463499 16.463499 0 0 1-16.16686 12.013905z m209.872538-120.287369a16.463499 16.463499 0 0 1-10.234067-29.663963l42.271147-29.663963a16.463499 16.463499 0 0 1 18.095017 0l46.127462 27.735805a16.31518 16.31518 0 0 1 5.636153 22.544612 16.463499 16.463499 0 0 1-22.544611 5.784473l-36.783314-22.247972-32.778679 22.396292a17.056779 17.056779 0 0 1-9.195829 3.114716z" fill="#333333" p-id="4449"></path></svg>
        <svg t="1721014115957" id="moon-icon" class="moon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="11914" width="200" height="200"><path d="M578.256332 591.814252v-82.970701M578.256332 604.385571a12.655127 12.655127 0 0 1-12.571318-12.571319v-82.970701a12.571318 12.571318 0 1 1 25.142636 0v82.970701a12.571318 12.571318 0 0 1-12.571318 12.571319z" fill="#F89B1B" p-id="11915"></path><path d="M598.873294 479.342858a36.959676 36.959676 0 0 1-27.573092-61.59946 52.380493 52.380493 0 1 0 62.521357 36.540632 36.875867 36.875867 0 0 1-34.948265 25.058828zM802.947694 370.307624v-82.970701M802.947694 382.878942a12.571318 12.571318 0 0 1-12.571318-12.571318v-82.970701a12.571318 12.571318 0 1 1 25.142636 0v82.970701a12.571318 12.571318 0 0 1-12.571318 12.571318z" fill="#F89B1B" p-id="11916"></path><path d="M823.9837 257.83623a36.959676 36.959676 0 0 1-27.6569-61.515651 52.129067 52.129067 0 1 0 64.616576 50.285273 53.050963 53.050963 0 0 0-2.011411-14.163685A36.875867 36.875867 0 0 1 823.9837 257.83623z" fill="#F89B1B" p-id="11917"></path><path d="M803.282929 328.822274a59.588049 59.588049 0 0 1 59.588049 59.588048v397.253658H743.694881v-397.253658a59.588049 59.588049 0 0 1 59.588048-59.588048zM581.776301 551.16699a143.145411 143.145411 0 0 1 143.145411 143.145411v143.229219H438.463272V694.312401a143.145411 143.145411 0 0 1 143.313029-143.145411z" fill="#612273" p-id="11918"></path><path d="M600.968514 198.667225l-49.111951-4.693292a8.380879 8.380879 0 0 1-7.039938-5.196145l-17.599845-42.658674a8.380879 8.380879 0 0 0-15.672244 0l-17.432228 42.658674a8.380879 8.380879 0 0 1-7.039938 5.196145l-49.11195 4.693292a8.380879 8.380879 0 0 0-4.777101 14.750347l36.959676 32.51781a8.380879 8.380879 0 0 1 2.681881 8.380878l-11.06276 45.67579a8.380879 8.380879 0 0 0 12.487509 9.302776L515.232123 285.074086a8.380879 8.380879 0 0 1 8.380879 0l40.982497 24.136931a8.380879 8.380879 0 0 0 12.571319-9.302776l-10.978952-45.675789a8.380879 8.380879 0 0 1 2.681882-8.380879L606.08085 213.417572a8.380879 8.380879 0 0 0-5.028528-14.750347z" fill="#FED150" p-id="11919"></path><path d="M470.897274 246.77347l1.927602-8.380879a8.380879 8.380879 0 0 0-2.681881-8.380879l-35.032074-30.506399a8.380879 8.380879 0 0 0-1.927602 13.912259l36.959676 32.51781a6.788512 6.788512 0 0 1 0.754279 0.838088zM603.98563 199.589122l-34.948265 30.674016a8.380879 8.380879 0 0 0-2.681881 8.380879l1.927602 8.380879a6.788512 6.788512 0 0 1 0.754279-0.838088L606.08085 213.417572a8.380879 8.380879 0 0 0-2.09522-13.82845zM575.406833 291.778789a8.380879 8.380879 0 0 1-10.643716 1.759985l-40.982498-24.053123a8.380879 8.380879 0 0 0-8.380879 0L474.249625 293.454965a8.380879 8.380879 0 0 1-10.643716-1.676176l-1.927602 8.380879a8.380879 8.380879 0 0 0 12.487509 9.302775l41.066307-24.388357a8.380879 8.380879 0 0 1 8.380879 0l40.982497 24.136931a8.380879 8.380879 0 0 0 12.571319-9.302776z" fill="#FED150" opacity=".5" p-id="11920"></path><path d="M434.608068 426.543321l-28.159753-2.681881a4.86091 4.86091 0 0 1-4.022822-3.017117l-10.057054-24.388357a4.86091 4.86091 0 0 0-8.967541 0l-9.973245 24.388357a4.693292 4.693292 0 0 1-4.022822 3.017117l-28.159753 2.681881a4.86091 4.86091 0 0 0-2.76569 8.380879l21.203623 18.605551a4.944719 4.944719 0 0 1 1.592367 4.777101L354.654484 484.455194a4.86091 4.86091 0 0 0 7.123747 5.363762l23.466461-13.82845a5.196145 5.196145 0 0 1 4.944718 0l23.466461 13.82845a4.86091 4.86091 0 0 0 7.123747-5.363762l-6.285659-26.064533a4.86091 4.86091 0 0 1 1.508558-4.777101l21.203624-18.605551a4.86091 4.86091 0 0 0-2.849499-8.380879z" fill="#FED150" p-id="11921"></path><path d="M360.102055 454.032604l1.173323-4.609484a4.944719 4.944719 0 0 0-1.592367-5.112336l-20.0303-17.683654a4.944719 4.944719 0 0 0-1.173323 8.380879l21.203623 18.605551zM436.284244 427.046174L416.253944 444.310784a4.86091 4.86091 0 0 0-1.508559 4.777101l1.173323 4.693292v-0.502852l21.203624-18.605551a4.86091 4.86091 0 0 0-0.838088-7.6266zM419.94153 479.845711a4.777101 4.777101 0 0 1-6.034233 1.005705l-23.46646-13.82845a5.196145 5.196145 0 0 0-4.944719 0l-23.466461 13.82845a4.777101 4.777101 0 0 1-6.034233-1.005705l-1.089514 4.609483a4.86091 4.86091 0 0 0 7.123747 5.363762l23.466461-13.82845a5.196145 5.196145 0 0 1 4.944719 0l23.46646 13.82845a4.86091 4.86091 0 0 0 7.123747-5.363762z" fill="#FED150" opacity=".5" p-id="11922"></path><path d="M635.413926 803.68287a414.685886 414.685886 0 0 1-175.998456-784.953114A9.805628 9.805628 0 0 0 453.967898 0.124205a513.831683 513.831683 0 1 0 567.050264 607.027056 9.805628 9.805628 0 0 0-18.186507-6.704704A414.350651 414.350651 0 0 1 635.413926 803.68287z" fill="#FED150" p-id="11923"></path><path d="M50.931434 292.868303a460.110249 460.110249 0 0 0 275.311871 359.455895 413.847798 413.847798 0 0 1 133.339782-633.594442A9.805628 9.805628 0 0 0 453.967898 0.124205 513.915492 513.915492 0 0 0 50.931434 292.868303z" fill="#FED150" opacity=".4" p-id="11924"></path><path d="M1006.016389 597.261823A513.664065 513.664065 0 0 1 3.914704 475.320036C3.244233 485.628517 2.657572 495.936998 2.657572 506.413097a513.831683 513.831683 0 0 0 1018.36059 100.570546 9.805628 9.805628 0 0 0-15.001773-9.72182zM231.539373 332.258434c0 7.458982 0.67047 14.917964 1.257132 22.293138A414.769695 414.769695 0 0 1 459.583087 18.729756 9.805628 9.805628 0 0 0 453.967898 0.124205a505.869848 505.869848 0 0 0-94.620122 20.868388 413.177328 413.177328 0 0 0-127.808403 311.265841z" fill="#FED150" opacity=".5" p-id="11925"></path><path d="M715.032275 421.514794m17.683654 0l141.217809 0q17.683654 0 17.683655 17.683654l0-0.083809q0 17.683654-17.683655 17.683655l-141.217809 0q-17.683654 0-17.683654-17.683655l0 0.083809q0-17.683654 17.683654-17.683654Z" fill="#EB3D72" p-id="11926"></path><path d="M205.139605 319.603307c4.441866-6.872321 22.041711-45.340555-11.817039-67.047031s-51.626214 8.380879-51.626214 8.380879a25.142637 25.142637 0 1 0 42.742482 27.489282s2.179029 5.950424-6.537085 18.437934-25.142637 12.236083-43.077718 0.754279-47.01673-65.789899-0.67047-138.787354c1.592367-2.514264 3.352352-4.693292 5.028527-7.039938a26.818812 26.818812 0 0 0-23.047417-2.430455 33.523515 33.523515 0 0 0-18.689359 17.683654c-31.260678 64.36515-22.628373 127.724594 21.203623 155.884347 48.944333 31.093061 82.048804-6.453277 86.49067-13.325597zM734.224488 931.491272c6.453277-2.681881 37.713955-21.45505 24.304548-53.386198s-40.647262-19.35983-40.647262-19.35983a21.874094 21.874094 0 1 0 16.761757 40.312027s-1.340941 5.363762-13.577023 9.973246S697.264812 905.259122 689.889638 888.497364s-1.340941-69.561295 67.047031-98.894371c2.346646-1.005705 4.693292-1.676176 7.039938-2.514263a31.931148 31.931148 0 0 0-1.927602-3.352352 28.578797 28.578797 0 0 0-38.635851-7.542791c-51.87764 30.841634-74.422204 81.545951-57.325212 122.277023 19.778874 46.262451 61.59946 35.786353 68.136546 33.020662zM279.813236 802.844782c-5.950424-3.687587-39.390131-18.354125-57.660447 11.146569s7.794217 44.334849 7.794217 44.334849a21.874094 21.874094 0 1 0 23.047417-36.875867s5.112336-2.011411 16.007479 5.279954 10.811334 21.622667 1.173323 37.211102-55.984271 41.317733-119.511333 2.430455c-2.179029-1.340941-4.106631-2.849499-6.118041-4.274249a22.376947 22.376947 0 0 0-1.676176 3.51997 28.662606 28.662606 0 0 0 16.342714 36.037779c55.146183 24.388357 109.538087 13.409406 132.920739-24.136931 26.399768-42.9101-6.369468-70.902235-12.319892-74.673631zM431.00429 694.312401h302.298301M733.302591 715.264598H431.00429a20.952197 20.952197 0 0 1 0-41.904394h302.298301a20.952197 20.952197 0 0 1 0 41.904394z" fill="#EB3D72" p-id="11927"></path><path d="M255.760113 683.082023m-30.171164 0a30.171164 30.171164 0 1 0 60.342328 0 30.171164 30.171164 0 1 0-60.342328 0Z" fill="#FED150" opacity=".4" p-id="11928"></path><path d="M356.246851 840.977781m-30.171164 0a30.171164 30.171164 0 1 0 60.342328 0 30.171164 30.171164 0 1 0-60.342328 0Z" fill="#FED150" opacity=".4" p-id="11929"></path><path d="M54.870447 472.135302m-30.171164 0a30.171164 30.171164 0 1 0 60.342328 0 30.171164 30.171164 0 1 0-60.342328 0Z" fill="#FED150" opacity=".4" p-id="11930"></path><path d="M561.410765 873.914635m-30.171164 0a30.171164 30.171164 0 1 0 60.342328 0 30.171164 30.171164 0 1 0-60.342328 0Z" fill="#FED150" opacity=".5" p-id="11931"></path><path d="M445.167976 825.13792m-19.862683 0a19.862683 19.862683 0 1 0 39.725365 0 19.862683 19.862683 0 1 0-39.725365 0Z" fill="#FED150" opacity=".5" p-id="11932"></path><path d="M149.406761 689.786726m-19.862683 0a19.862683 19.862683 0 1 0 39.725365 0 19.862683 19.862683 0 1 0-39.725365 0Z" fill="#FED150" opacity=".5" p-id="11933"></path><path d="M132.225959 633.299603m-18.940786 0a18.940786 18.940786 0 1 0 37.881572 0 18.940786 18.940786 0 1 0-37.881572 0Z" fill="#FED150" opacity=".4" p-id="11934"></path><path d="M475.339139 906.935297m-18.940786 0a18.940786 18.940786 0 1 0 37.881573 0 18.940786 18.940786 0 1 0-37.881573 0Z" fill="#FED150" opacity=".4" p-id="11935"></path></svg>

</div>
      </div>
      <div class="leftlist">
        <svg @click="navigateTo('Catalog')" id="Catalog" t="1719471435071" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="18790" width="200" height="200"><path d="M867.995 459.647h-711.99c-27.921 0-52.353 24.434-52.353 52.353s24.434 52.353 52.353 52.353h711.99c27.921 0 52.353-24.434 52.353-52.353s-24.434-52.353-52.353-52.353z" p-id="18791" fill="#bfbfbf"></path><path d="M867.995 763.291h-711.99c-27.921 0-52.353 24.434-52.353 52.353s24.434 52.353 52.353 52.353h711.99c27.921 0 52.353-24.434 52.353-52.353s-24.434-52.353-52.353-52.353z" p-id="18792" fill="#bfbfbf"></path><path d="M156.005 260.709h711.99c27.921 0 52.353-24.434 52.353-52.353s-24.434-52.353-52.353-52.353h-711.99c-27.921 0-52.353 24.434-52.353 52.353s24.434 52.353 52.353 52.353z" p-id="18793" fill="#bfbfbf"></path>
          <title class="tooltip">目录</title>
        </svg>
        <svg @click="navigateTo('Outline')" id="Outline" t="1719471418244" class="icon" viewBox="0 0 1126 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2304" width="200" height="200"><path d="M142.234 0a142.234 142.234 0 0 1 56.883 272.589v210.944h113.715c15.718 0 28.467 12.8 28.467 28.467v56.883a28.467 28.467 0 0 1-28.467 28.467H199.168v263.117c0 16.538 3.43 31.488 8.704 42.087l2.048 3.686a34.1 34.1 0 0 0 1.894 2.918l0.87 1.024h100.148c15.718 0 28.467 12.8 28.467 28.468v56.883A28.467 28.467 0 0 1 312.832 1024H207.258c-72.807 0-119.399-73.267-121.856-156.774l-0.052-6.759V272.59A142.234 142.234 0 0 1 142.182 0z m886.988 853.35a51.2 51.2 0 0 1 51.2 51.2v68.25a51.2 51.2 0 0 1-51.2 51.2H562.79a51.2 51.2 0 0 1-51.2-51.2v-68.25a51.2 51.2 0 0 1 51.2-51.2h466.432z m0-398.233a51.2 51.2 0 0 1 51.2 51.2v68.25a51.2 51.2 0 0 1-51.2 51.2H562.79a51.2 51.2 0 0 1-51.2-51.2v-68.199a51.2 51.2 0 0 1 51.2-51.2h466.432z m0-398.234a51.2 51.2 0 0 1 51.2 51.2v68.25a51.2 51.2 0 0 1-51.2 51.2H562.79a51.2 51.2 0 0 1-51.2-51.2v-68.25a51.2 51.2 0 0 1 51.2-51.2h466.432z" fill="#bfbfbf" p-id="2305"></path>
          <title class="tooltip">大纲</title>
        </svg>
        <svg @click="navigateTo('OCR')" id="OCR" t="1719471387059" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2344" width="200" height="200"><path d="M1022.54 731.84v182.08c0 60.23-49.01 109.25-109.25 109.25H694.81c-20.14 0-36.42-16.28-36.42-36.42s16.28-36.42 36.42-36.42H913.3c20.1 0 36.42-16.31 36.42-36.41V731.84c0-20.14 16.27-36.42 36.42-36.42 20.13 0 36.4 16.28 36.4 36.42zM294.07 950.33H111.99c-20.06 0-36.41-16.31-36.41-36.41V731.84c0-20.14-16.31-36.42-36.42-36.42-20.1 0-36.41 16.28-36.41 36.42v182.08c0 60.23 49.01 109.25 109.24 109.25h182.08c20.1 0 36.42-16.28 36.42-36.42s-16.32-36.42-36.42-36.42zM38.16 328.1c20.1 0 36.42-16.31 36.42-36.41V109.61c0-20.07 16.35-36.42 36.41-36.42h182.08c20.1 0 36.42-16.31 36.42-36.41 0-20.1-16.31-36.42-36.42-36.42H110.99C50.76 0.36 1.75 49.38 1.75 109.61v182.08c0 20.1 16.31 36.41 36.41 36.41zM914.3 0.36H695.81c-20.14 0-36.42 16.31-36.42 36.42 0 20.1 16.28 36.41 36.42 36.41H914.3c20.1 0 36.42 16.35 36.42 36.42v182.08c0 20.1 16.27 36.41 36.42 36.41 20.14 0 36.41-16.31 36.41-36.41V109.61C1023.54 49.38 974.53 0.36 914.3 0.36zM383.4 509.78c0 97.6-55.2 156-136.4 156s-136.4-58.4-136.4-156 55.2-152.8 136.4-152.8 136.4 55.6 136.4 152.8z m-72.8 0c0-57.6-24.4-91.6-63.6-91.6s-63.2 34-63.2 91.6c0 58 24 94.4 63.2 94.4s63.6-36.4 63.6-94.4z m246.8 94.4c-42 0-69.2-34.4-69.2-93.6 0-58 31.6-92.4 70-92.4 21.2 0 36.8 9.6 51.6 23.2l37.6-45.6c-20.4-20.8-51.6-38.8-90.4-38.8-75.6 0-142 56.8-142 156 0 100.8 64 152.8 139.6 152.8 38.8 0 72-14.8 97.2-44l-37.6-44.8c-14 15.2-33.2 27.2-56.8 27.2z m302.4-62l66.4 118h-80l-54.8-104.8H757v104.8h-71.6v-297.6h109.2c63.6 0 116.4 21.6 116.4 93.6 0 43.6-20.4 71.6-51.2 86z m-18.8-86c0-28-18-37.2-52-37.2h-32v80h32c34 0 52-14.8 52-42.8z" p-id="2345" fill="#bfbfbf"></path>
          <title class="tooltip">图片识别</title>
        </svg>
        <svg @click="navigateTo('Voice')" id="Voice" t="1719471369078" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4166" width="200" height="200"><path d="M923.648 108.088889c21.902222 0 39.594667 15.815111 42.382222 36.920889l0.398222 5.859555V820.906667a42.325333 42.325333 0 0 1-36.977777 42.439111l-5.802667 0.341333H531.797333a35.555556 35.555556 0 0 1-5.233777-70.712889l5.233777-0.398222h330.695111c15.36 0 28.103111-11.207111 30.492445-25.884444l0.398222-4.949334V212.48a30.947556 30.947556 0 0 0-25.884444-30.435556l-5.006223-0.455111H532.764444a36.522667 36.522667 0 0 1-36.522666-36.522666c0-18.773333 13.312-33.962667 31.061333-36.579556l5.461333-0.398222h390.826667zM560.924444 354.076444c19.911111 0 36.465778 18.090667 36.465778 39.424 0 141.368889-94.435556 263.793778-221.809778 289.962667l-14.563555 2.503111v132.096c0 19.342222-13.653333 36.067556-31.118222 38.968889l-5.347556 0.398222c-18.204444 0-33.450667-14.961778-36.124444-33.678222l-0.398223-5.688889v-132.096l-2.503111-0.341333C155.875556 665.144889 57.344 546.360889 51.484444 406.641778L51.2 393.500444c0-21.617778 16.497778-39.424 36.977778-39.424 19.968 0 36.522667 18.090667 36.522666 39.424 0 119.239111 89.770667 216.177778 199.850667 216.177778 110.08 0 199.850667-96.938667 199.850667-216.177778 0-21.333333 16.497778-39.424 36.522666-39.424z m259.185778 259.413334c19.114667 0 35.100444 16.099556 35.100445 35.157333a33.564444 33.564444 0 0 1-9.784889 24.348445 35.157333 35.157333 0 0 1-19.626667 10.24l-5.688889 0.455111h-177.607111a35.441778 35.441778 0 0 1-35.043555-35.100445c0-17.351111 13.198222-32.142222 29.923555-34.702222l5.12-0.341333h177.607111zM324.835556 123.448889c65.592889 0 118.897778 53.304889 118.897777 118.897778v170.894222c0 65.536-53.304889 118.897778-118.897777 118.897778a119.523556 119.523556 0 0 1-119.864889-118.897778V242.346667c0-65.592889 53.76-118.897778 119.864889-118.897778z m495.331555 329.784889c19.114667 0 35.100444 16.042667 35.100445 35.157333a33.564444 33.564444 0 0 1-9.728 24.291556 35.271111 35.271111 0 0 1-19.683556 10.24l-5.688889 0.455111h-177.607111a35.498667 35.498667 0 0 1-35.043556-35.100445c0-17.294222 13.198222-32.085333 29.923556-34.702222l5.12-0.341333h177.607111z m0-159.288889c19.114667 0 35.100444 15.985778 35.100445 35.100444a33.564444 33.564444 0 0 1-9.728 24.291556 35.214222 35.214222 0 0 1-19.683556 10.24l-5.688889 0.455111h-177.607111a35.441778 35.441778 0 0 1-35.043556-35.043556c0-17.351111 13.198222-32.142222 29.923556-34.702222l5.12-0.398222h177.607111z" fill="#bfbfbf" p-id="4167"></path>
          <title class="tooltip">语音识别</title>
        </svg>
        <svg @click="navigateTo('Translate')" id="Translate" t="1719471340950" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="9962" width="200" height="200"><path d="M512 1024C230.4 1024 0 793.6 0 512S230.4 0 512 0s512 230.4 512 512-230.4 512-512 512z m0-960C265.6 64 64 265.6 64 512s201.6 448 448 448 448-201.6 448-448S758.4 64 512 64z m268.8 422.4c-60.8-6.4-118.4-22.4-169.6-51.2-54.4 25.6-115.2 44.8-172.8 57.6l-28.8-51.2c51.2-9.6 102.4-25.6 150.4-44.8-32-28.8-57.6-64-70.4-105.6H448V240h304v51.2c-19.2 44.8-48 83.2-86.4 112 44.8 16 89.6 28.8 134.4 32l-19.2 51.2z m-92.8-192H544c16 32 38.4 57.6 67.2 76.8 28.8-19.2 57.6-44.8 76.8-76.8zM265.6 265.6L307.2 224c38.4 28.8 70.4 57.6 102.4 92.8l-41.6 41.6c-28.8-35.2-64-67.2-102.4-92.8z m99.2 396.8c16-16 32-35.2 51.2-54.4l16 64c-35.2 38.4-73.6 76.8-115.2 108.8l-22.4-54.4c9.6-9.6 16-22.4 16-35.2v-227.2H224v-57.6h140.8v256z m214.4-83.2h-112v-54.4h112v-51.2h57.6v51.2h121.6v54.4h-121.6V640h150.4v57.6h-150.4V800h-57.6v-102.4h-137.6V640h137.6v-60.8z" p-id="9963" fill="#bfbfbf"></path>
          <title class="tooltip">翻译</title>
        </svg>
        <svg @click="navigateTo('Summarize')" id="Summarize" t="1719471303821" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2312" width="200" height="200"><path d="M841 315.6H641c-28.7 0-52-23.3-52-52V82h46v181.6c0 3.3 2.7 6 6 6h200v46z" fill="#bfbfbf" p-id="2313"></path><path d="M804 966H215c-29.2 0-53-23.8-53-53V119c0-29.2 23.8-53 53-53h41c12.7 0 23 10.3 23 23s-10.3 23-23 23h-41c-3.9 0-7 3.1-7 7v794c0 3.9 3.1 7 7 7h589c3.9 0 7-3.1 7-7V288.5L609.3 112H426c-12.7 0-23-10.3-23-23s10.3-23 23-23h192c5.6 0 11 2 15.1 5.7l216 189c5 4.4 7.9 10.7 7.9 17.3v635c0 29.2-23.8 53-53 53zM364.9 112h-39c-12.7 0-23-10.3-23-23s10.3-23 23-23h39c12.7 0 23 10.3 23 23s-10.3 23-23 23z" fill="#bfbfbf" p-id="2314"></path><path d="M307 372h413c8.3 0 15 6.7 15 15s-6.7 15-15 15H307c-8.3 0-15-6.7-15-15s6.7-15 15-15zM307 498h413c8.3 0 15 6.7 15 15s-6.7 15-15 15H307c-8.3 0-15-6.7-15-15s6.7-15 15-15zM307 624h413c8.3 0 15 6.7 15 15s-6.7 15-15 15H307c-8.3 0-15-6.7-15-15s6.7-15 15-15zM307 750h413c8.3 0 15 6.7 15 15s-6.7 15-15 15H307c-8.3 0-15-6.7-15-15s6.7-15 15-15zM307 246h231c8.3 0 15 6.7 15 15s-6.7 15-15 15H307c-8.3 0-15-6.7-15-15s6.7-15 15-15z" fill="#bfbfbf" p-id="2315"></path><path d="M610 481h71c7.7 0 14 6.3 14 14v35c0 7.7-6.3 14-14 14h-71c-7.7 0-14-6.3-14-14v-35c0-7.7 6.3-14 14-14zM346 734h71c7.7 0 14 6.3 14 14v35c0 7.7-6.3 14-14 14h-71c-7.7 0-14-6.3-14-14v-35c0-7.7 6.3-14 14-14zM346 230h71c7.7 0 14 6.3 14 14v35c0 7.7-6.3 14-14 14h-71c-7.7 0-14-6.3-14-14v-35c0-7.7 6.3-14 14-14z" fill="#bfbfbf" p-id="2316"></path>
          <title class="tooltip">摘要</title>
        </svg>
        <svg @click="navigateTo('Style_library')" id="Style_library" t="1719471218475" class="icon" viewBox="0 0 1026 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2347" width="200" height="200"><path d="M944.4 311.8c-32.7-2.3-63.4 3.5-101.5 54.3s-152.3 20.7-137.5-41c6.6-17.8 7.7-36.4 70.3-66.8 62.6-30.4 36.1-100.4 9.6-115 0 0-241.9-138.7-580.3 60.9-93 54-265.5 251.1-183.5 459.2C73.1 787.7 162.8 858.8 308.3 905c145.5 46.2 314.7 14.7 400.4-29.3 85.7-44 227.8-109.4 294.4-284.2 66.5-174.8-26-277.5-58.7-279.7z m-850 179.6c-3.8-26.8 24.3-53 62.9-58.5 38.5-5.5 72.9 11.8 76.7 38.6 3.8 26.8-24.3 53-62.9 58.5s-72.9-11.8-76.7-38.6z m121 203.6c-40.5 5.8-76.7-12.4-80.7-40.6-4-28.2 25.6-55.7 66.1-61.5 40.5-5.8 76.6 12.4 80.7 40.6 4.1 28.2-25.5 55.7-66.1 61.5z m18.4-325.2c-38.9 5.5-73.5-11.9-77.4-39-3.8-27.1 24.5-53.5 63.4-59s73.5 11.9 77.4 39-24.6 53.4-63.4 59z m172.9 468.8c-44.2 9.3-85.2-8.1-91.7-38.9-6.4-30.7 24.1-63.2 68.3-72.4 44.2-9.3 85.2 8.1 91.7 38.9 6.4 30.7-24.2 63.1-68.3 72.4z m28.9-582c-37 5.3-70-11.3-73.6-37.1-3.7-25.7 23.4-50.9 60.4-56.1 37-5.3 70 11.3 73.6 37.1 3.6 25.7-23.4 50.8-60.4 56.1z" p-id="2348" fill="#bfbfbf"></path>
          <title class="tooltip">样式库</title>
        </svg>
      </div>
      <div class="toolBar">
         <router-view></router-view>
      </div>
    </div>
    <div class="editor">
      <!-- <p>store.isShow: {{ store.isShow }}</p> -->
      <div v-if="showMind" class="jsmind_wrapper">
        <Loading v-if="showLoading2"/>
        <div id="jsmind_btn">
          <button class="jsmind_button" @click="backMindmap()">返回</button>
          <button class="jsmind_button" @click="saveMindmap()">保存</button>
        </div>
        <div id="jsmind_container"></div>

      </div>
      <div v-if="store.isShow" class="editorcard">
        <div class="toptools">
          <EditorMenu :editor="editor"/>
          <div class="topBtn">
          <div id="switch" @click="toggleTheme"></div>
          <!-- <button class="topButton" @click="toggleTheme()">昼夜切换</button> -->
          <button class="topButton" @click="autoMindmap()">思维导图</button>
          <button class="topButton" @click="autoFormat()">格式化</button>
          <button class="topButton" @click="saveHTMLText()">Save</button>
        </div>
        </div>
        <div class="editcont">
          <Loading v-if="showLoading"/>
          <ContextMenu>
          <EditorContent @mousescroll="" @mousedown="" @mousemove=""
            @mouseup="selecttext($event)" style="padding: 8px; color: var(--textColor);" :editor="editor" />
          </ContextMenu>
        </div>

        <div class="bottomcount">
          字数统计:
          {{ editor?.storage.characterCount.characters() }}
        </div>
      </div>
      <div v-else-if="store.editorisShow">
        <Style_editor></Style_editor>
      </div>
      <div v-else>
        <Welcome></Welcome>
      </div>
    </div>


    <!-- <div class="righttools">
      
    </div> -->
  </div>
</template>
<script lang="ts" setup>
import { Brush, EditPen, } from '@element-plus/icons-vue'
import { defineComponent, onMounted, onBeforeUnmount, ref, watch, computed, nextTick } from 'vue';
import { Editor, EditorContent, useEditor, BubbleMenu } from '@tiptap/vue-3';
import { storeToRefs } from 'pinia'
import Underline from '@tiptap/extension-underline'
import ContextMenu from '../../components/ContextMenu.vue'
import Loading from '../../components/Loading.vue'
import OpenAnimation from '../../components/OpenAnimation.vue'
// 列表
import ListItem from '@tiptap/extension-list-item'
import OrderedList from '@tiptap/extension-ordered-list'
import BulletList from '@tiptap/extension-bullet-list'
// 左侧
import misakaImg from '../../assets/images/Misaka Mikoto.webp'
import Catalog from './Catalog/index.vue'
import Outline from './Outline/index.vue'
import OCR from './OCR/index.vue'
import Voice from './Voice/index.vue'
import Style_library from './Style_library/index.vue'
// 代码
import CodeBlockLowlight from '@tiptap/extension-code-block-lowlight'
import css from 'highlight.js/lib/languages/css'
import js from 'highlight.js/lib/languages/javascript'
import ts from 'highlight.js/lib/languages/typescript'
import html from 'highlight.js/lib/languages/xml'
import { common, createLowlight } from 'lowlight'
// 字数统计
import CharacterCount from '@tiptap/extension-character-count'
import Heading from '@tiptap/extension-heading'
import StarterKit from '@tiptap/starter-kit'
import Placeholder from '@tiptap/extension-placeholder'
import { UndoRound, MoreHorizOutlined } from '@vicons/material'
import TaskItem from '@tiptap/extension-task-item'
import TaskList from '@tiptap/extension-task-list'
import Welcome from './Welcome/index.vue'
import Style_editor from './Style_editor/index.vue'
import { Paragraph } from '@tiptap/extension-paragraph';
// 使用Pinia
import { useEditorStore } from '../../router/index.ts'
import EditorMenu from './EditorMenu/index.vue'
import { defineStore } from 'pinia'
import { ElMessage } from 'element-plus';
import axios from 'axios'
import { useRouter } from 'vue-router';
import { mainStore } from '../../store/index.ts';
import { Extension } from '@tiptap/core'

import lightImage from '@/assets/images/light_background.jpg';
import darkImage from '@/assets/images/dark_background.jpg';
import ThemeIcon from '@/components/ThemeIcon.vue';

import 'jsmind/style/jsmind.css';
import 'jsmind/screenshot'
import jsMind from 'jsmind';
import domtoimage from 'dom-to-image';

const router = useRouter();
const lowlight = createLowlight()
lowlight.register({ html, ts, css, js })
const editorStore = useEditorStore()
const store = mainStore();
const aipolish = ref("")
const filecont = ref(null);
const aicontinuation = ref("")
const visiblemenu = ref(false)
const position = ref({
  top: 0,
  left: 0
})
const theme = ref('')
const editorContent = ref('');
const showLoading = ref(false);
const showLoading2 = ref(false);
const showMind = ref(false);
const username = localStorage.getItem('username');

store.setUsername(username);

const mind = {
  "meta": {
    "name": "Hypercube",
    "author": "haibara",
    "version": "0.2"
  },
  "format": "node_tree",
  "data": {
    "id": "root",
    "topic": "jsMind",
    "children": [
      
    ]
  }
};

let jm;

function navigateTo(componentName) {
  router.push({ name: componentName });

  let currentIcon = document.getElementById(componentName);
  const svgIcons = document.querySelectorAll('.icon');
  currentIcon.querySelectorAll('path').forEach(path => {
    path.style.fill = '#ffffff';
  });
  svgIcons.forEach(svgIcon => {
    if (svgIcon.id !== componentName) {
      svgIcon.querySelectorAll('path').forEach(path => {
        path.style.fill = '';
      });
    }
  });
}
onMounted(() => {
  store.initializeTheme();
  theme.value = store.theme;
  store.setIsOpen(false);
});

const currentImage = computed(() => {
  return store.theme === 'light' ? lightImage : darkImage;
});

const ExtendedStyle = Extension.create({
  name: 'extendedStyle',
  addGlobalAttributes() {
    return [
      {
        types: ['heading', 'paragraph', 'bulletList', 'orderedList'],
        attributes: {
          style: {
            default: '',
            parseHTML: element => {
              const style = element.getAttribute('style') || '';
              return style;
            },
            renderHTML: attributes => {
              return { style: attributes.style };
            },
          },
        },
      },
    ];
  },
  // @ts-ignore
  addCommands() {
    return {
      setElementStyle: (style) => ({ commands }) => {
        return commands.updateAttributes('heading', { style }) ||
               commands.updateAttributes('paragraph', { style }) ||
               commands.updateAttributes('bulletList', { style }) ||
               commands.updateAttributes('orderedList', { style });
      },
    };
  },
});



const sunIcon = document.getElementById("sun-icon");
  const moonIcon = document.getElementById("moon-icon");

watch(() => store.theme, (newTheme) => {
  const sunIcon = document.getElementById("sun-icon");
  const moonIcon = document.getElementById("moon-icon");
  if (sunIcon && moonIcon) {
    if (newTheme === 'dark') {
      sunIcon.classList.remove("show-sun");
      sunIcon.classList.add('hide-sun');
      setTimeout(() => {
        moonIcon.classList.remove("hide-moon");
        moonIcon.classList.add('show-moon');
    }, 300);
    } else {

      moonIcon.classList.remove("show-moon");
      moonIcon.classList.add('hide-moon');
      setTimeout(() => {
        sunIcon.classList.remove("hide-sun");
        sunIcon.classList.add('show-sun');
    }, 300);

    }
  }
});

// 初始化时设置图标状态
const initIcons = () => {
  const sunIcon = document.getElementById("sun-icon");
  const moonIcon = document.getElementById("moon-icon");
  if (sunIcon && moonIcon) {
    if (store.theme === 'dark') {
      sunIcon.classList.add('hide-sun');      
      moonIcon.classList.add('show-moon');
    } else {
      moonIcon.classList.add('hide-moon');
      sunIcon.classList.add('show-sun');
    }
  }
};

onMounted(() => {
  initIcons();
});



store.initializeEditor();
const { editor } = storeToRefs(store);

const saveHTMLText = () => {
  if (editor.value) {
    editorContent.value = editor.value.getHTML();
  }
  let styleid = 1;
  if(store.usedStyleID){
    styleid = store.usedStyleID;
  }
  let formdata = new FormData();
  formdata.append("username", store.username);
  formdata.append("id", store.openNoteID);
  // @ts-ignore
  formdata.append("note", editorContent.value);
  // @ts-ignore
  formdata.append("styleId", styleid);
  axios({
    method: 'post',
    url: `${store.ipAddress}/api/saveNote`,
    data: formdata,
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  }).then(res => {
    if(res.data.ret == 0) alert("保存成功");
  }).catch(error => {
    console.error("There was an error!", error);
  });
};


const autoFormat = () => {
  showLoading.value = true;
  if (editor.value) {
    editorContent.value = editor.value.getHTML();
  }
  let formdata = new FormData();
  formdata.append("text", editorContent.value);
  axios({
    method: 'post',
    url: `${store.ipAddress}/api/autoFormat`,
    data: formdata,
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  }).then(res => {
  if(res.data.ret == 0){
    const htmlContent = res.data.res;
    store.setHTMLContent(htmlContent);
    showLoading.value = false;
  }
  else{
    alert(res.data.msg);
  }
  })
}

const autoMindmap = async () => {
  showLoading2.value = true;
  showMind.value = true;

  if (editor.value) {
    editorContent.value = editor.value.getHTML();
  }

  let formData1 = new FormData();
  formData1.append('username', store.username);

  try {
    // 第一个请求，获取 noteName
    const res1 = await axios({
      method: 'post',
      url: `${store.ipAddress}/api/pullNoteList`,
      data: formData1,
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });

    let noteName = '';
    for (let i = 0; i < res1.data.noteList.length; i++) {
      if (res1.data.noteList[i][0] == store.openNoteID) {
        noteName = res1.data.noteList[i][1];
        break;
      }
    }

    if (!noteName) {
      throw new Error('Note name not found');
    }

    // 第二个请求，自动生成思维导图
    let formData2 = new FormData();
    formData2.append("text", editorContent.value);
    formData2.append("noteName", noteName);

    const res2 = await axios({
      method: 'post',
      url: `${store.ipAddress}/api/autoMindmap`,
      data: formData2,
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });

    if (res2.data.ret) {
      alert(res2.data.msg);
    } else {
      console.log(mind.data);
      const jsonString = res2.data.res;
      const jsonData = JSON.parse(jsonString); 
      mind.data = jsonData;
      var options = {
        container: 'jsmind_container',
        theme: 'primary',
        editable: true,
      };
      jm = new jsMind(options);
      jm.show(mind);
      showLoading2.value = false;
    }
  } catch (error) {
    console.error('Error:', error);
  }
};

const backMindmap = () => {
  showMind.value = false;
};

const saveMindmap = () => {
  jm.shoot();
};

watch(() => store.htmlContent, (newContent) => {
  if (editor.value) {
    editor.value.commands.setContent(newContent, 'html');
  }
  stopLoading();
});

watch(() => store.openNoteID, () => {
  loading();
});

watch(() => store.usedStyleID, () => {
  loading();
});

watch(() => store.isLoading, () => {
  stopLoading();
  store.isLoading = false;
});

// 获取选中的文字
const selecttext = (e: MouseEvent) => {
    const { from, to } = editor.value.state.selection;
    if (from !== to) {
        const selection = window.getSelection().toString();
        store.setContent(selection);
    }
    else {
        store.setContent('');
    }
}

// 润色函数
const polishSelected=(text)=>{
    var formData = new FormData();
    formData.append('text', text);

    axios({
        method: 'post', 
        url: `${store.ipAddress}/api/polish`, 
        data: formData, 
        headers:{'Content-Type': 'multipart/form-data'}}
    )
    .then(response => {
        let responseData = response.data;
        if (responseData.ret === 0) {
            editor.value.chain().focus().deleteSelection().insertContent(responseData.res).run();
        } else {
            ElMessage({message: '润色失败：' + responseData.msg, type: 'error', duration: 5 * 1000, grouping: true});
        }
    })
    .catch(error => {
        console.error('Error posting data:', error);
        ElMessage({message: '润色失败：网络错误，请稍后重试！', type: 'error', duration: 5 * 1000, grouping: true});
    })
    .finally(() => {
        stopLoading();
    });
}

// 修改病句函数 
const correctSelected=(text)=>{
    var formData = new FormData();
    formData.append('text', text);

    axios({
        method: 'post', 
        url: `${store.ipAddress}/api/correct`, 
        data: formData, 
        headers:{'Content-Type': 'multipart/form-data'}}
    )
    .then(response => {
        let responseData = response.data;
        if (responseData.ret === 0) {
            editor.value.chain().focus().deleteSelection().insertContent(responseData.res).run();
        } else {
            ElMessage({message: '修改失败：' + responseData.msg, type: 'error', duration: 5 * 1000, grouping: true});
        }
    })
    .catch(error => {
        console.error('Error posting data:', error);
        ElMessage({message: '修改失败：网络错误，请稍后重试！', type: 'error', duration: 5 * 1000, grouping: true});
    })
    .finally(() => {
        stopLoading();
    });
}

// 剪切函数
const deleteSelected = () => {
    editor.value.chain().focus().deleteSelection().run();
}

// 复制函数
const copySelected = () => {
    navigator.clipboard.writeText(store.content);
}

// 粘贴函数
const pasteSelected = (text) => {
    navigator.clipboard.readText().then(clipText => {
        editor.value.chain().focus().deleteSelection().insertContent(clipText).run();
    });
}
const toggleTheme = () => {
  const sw = document.getElementById('switch');
  if (sw) {
    sw.classList.add('pull');
    console.log('Added pull class'); // 调试用
    setTimeout(() => {
      sw.classList.remove('pull');
      console.log('Removed pull class'); // 调试用
    }, 600);
  }

  store.toggleTheme();

};



// 监听菜单事件
watch(() => store.select, (select) => {
    if (select === 'polish') {
        loading();
        polishSelected(store.content);
    }
    if (select === 'correct') {
        loading();
        correctSelected(store.content);
    }
    if (select === 'delete') {
        deleteSelected();
    }
    if (select === 'copy') {
        copySelected();
    }
    if (select === 'paste') {
        pasteSelected(store.content);
    }
});


const loading = () => {
    showLoading.value = true;
}

const stopLoading = () => {
    showLoading.value = false;
}
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

.EditMain {
  position: relative;
  width: 100w;
  height: 98.5vh;

  display: grid;
  grid-template-columns: 25% 75%;

}

.background {
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center;
        position: fixed;
        z-index: -1;
    }

.lefttools {
  position: relative;
  display: flex;
  background-color: rgba(255, 255, 255, 0);
  height: 98.5vh;
  width: 100%;
  display: grid;
  grid-template-rows: 10% 10% 80%;
}

.lefttop {
  position: relative;
  display: flex;
  align-items: center;
  background-color: var(--backgroundColor);
  width: 95%;
  height: 90%;
  left: 2.5%;
  top: 5%;
  border-radius: 5px;
  overflow: hidden;
}

#theme-icon {
  position: absolute;
  top: 10px; /* 根据需要调整 */
  right: 10px; /* 根据需要调整 */
  width: 5%; /* 根据需要调整 */
  height: 5%; /* 根据需要调整 */
}


.lefttop img{
  height:auto;
}

.icon{
  position: relative;
  max-width: 40%;
  max-height: 40%;
  object-fit: contain;
  cursor: pointer;
}

.icon:hover path{
  fill: #ffffff
}

.username-display {
  padding-left: 5%;
  margin: 0; 
  color: var(--titleColor);
  overflow-x: hidden;
}
.leftlist{
  position: relative;
  display: flex;
  align-items: center; 
  justify-content: center; 
  background-color: var(--backgroundColor);
  width: 95%;
  height: 100%;
  left: 2.5%;
  top: 2.5%;
  object-fit: contain;
  border-radius: 5px;
}

.leftlist svg{
  position: relative;
  max-width: 40%;
  max-height: 40%;
  object-fit: contain;
  cursor: pointer;
  filter: invert(var(--invert));
}



.toolBar {
  position: relative;
  background-color: var(--backgroundColor);
  width: 95%;
  height: 100%;
  left: 2.5%;
  bottom: 2.5%;
  top: 1%;
  border-radius: 5px;

}



*,
* *,
*::before,
*::after {
  box-sizing: border-box;
}


#switch {
  position: fixed;
  height: 100px;
  width: 2px;
  background: var(--titleColor);
  right: 22%;
  top: -60px;
  cursor: pointer;
  z-index: 2;
}

#switch::after {
  content: '';
  position: absolute;
  border: 2px solid var(--titleColor);
  border-radius: 50%;
  width: 22px;
  height: 22px;
  left: -10px;
  bottom: -20px;
  z-index: 2;
}

@keyframes line {
  0% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(30px);
  }
  100% {
    transform: translateY(0);
  }
}

.pull {
  animation: line 0.5s ease;
}


.editor {
  position: relative;
  display: grid;
}

.jsmind_wrapper {
  position: absolute;
  width: 95%;
  height: 95%;
  left: 2.5%;
  top: 2.5%;
  background-color: var(--openbackColor);
  z-index: 1;
}
#jsmind_btn{
  position: absolute;
  width: 100%;
  height: 42px;
  top: 0;
  background-color: #adb5bd;
}
#jsmind_container {
  position: absolute;
  width: 100%;
  height: calc(100% - 42px);
  top: 42px;
  background-color: var(--openbackColor);
  z-index: 1;
}
.jsmind_button {
  position: relative;
  background-color: var(--btnColor);
  color: var(--titleColor);
  border: 1.5px solid var(--titleColor);
  bottom: 0;
  z-index: 1;
  top: 0%;
  left: 86.5%;
  margin-left: 8px;
}

.editorcard {
  position: relative;
  width: 95%;
  height: 95%;
  left: 2.5%;
  top: 2.5%;
  display: grid;
  grid-template-rows: 5% 91% 4%;
  border-radius: 5px;
}



.toptools {
  display: flex;
  background-color: var(--toptools);
  border-bottom: 1px dashed #9ca19f65;
}


.topBtn {
  position: relative;
  display: flex;
  /* max-height: 50px; */
  margin-right: 0px;
  margin-left: auto;
}
.topButton {
  background-color: var(--btnColor);
  color: var(--titleColor);
  border: 1.5px solid var(--titleColor);
  max-height: 100%;
  margin-right: 5px;
}



.bottomcount {
  background-color: var(--countColor);
  border-top: 5px;
  height: 100%;
  width: 100%;
  display: grid;
  grid-template-columns: 100%;
  grid-template-rows: 100%;
  justify-items: center;
  align-items: center;
}

.editcont {
  position: relative;
  max-height: 88vh;
  width: 100%;
  overflow-y: auto;
  object-fit: contain;
  background-color: var(--editorColor);
}

.ProseMirror {
  overflow: hidden !important;
}
</style>

<style lang="scss">
b {
  font-weight: bold;
}

.ProseMirror {
  overflow-y: scroll;
}

.ProseMirror p {
  margin: 0;
}

.ProseMirror:focus {
  outline: none;
}

.tiptap p.is-editor-empty:first-child::before {
  color: #adb5bd;
  content: attr(data-placeholder);
  float: left;
  height: 0;
  pointer-events: none;
}


.tiptap {
  >*+* {
    margin-top: 0.75em;
  }

  ul {
    padding: 0 2rem;
    list-style: square;
  }

  ol {
    padding: 0 2rem;
    list-style: decimal;
  }

  table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 100%;
    margin: 0;
    overflow: hidden;

    td,
    th {
      min-width: 1em;
      border: 2px solid #ced4da;
      padding: 3px 5px;
      vertical-align: top;
      box-sizing: border-box;
      position: relative;

      >* {
        margin-bottom: 0;
      }
    }

    th {
      font-weight: bold;
      text-align: left;
      background-color: #f1f3f5;
    }

    .selectedCell:after {
      z-index: 2;
      position: absolute;
      content: '';
      left: 0;
      right: 0;
      top: 0;
      bottom: 0;
      background: rgba(200, 200, 255, 0.4);
      pointer-events: none;
    }

    .column-resize-handle {
      position: absolute;
      right: -2px;
      top: 0;
      bottom: -2px;
      width: 4px;
      background-color: #adf;
      pointer-events: none;
    }

    p {
      margin: 0;
    }
  }

  pre {
    background: #0d0d0d;
    color: #fff;
    font-family: 'JetBrainsMono', monospace;
    padding: 0.75rem 1rem;
    border-radius: 0.5rem;

    code {
      color: inherit;
      padding: 0;
      background: none;
      font-size: 0.8rem;
    }

    .hljs-comment,
    .hljs-quote {
      color: #616161;
    }

    .hljs-variable,
    .hljs-template-variable,
    .hljs-attribute,
    .hljs-tag,
    .hljs-name,
    .hljs-regexp,
    .hljs-link,
    .hljs-name,
    .hljs-selector-id,
    .hljs-selector-class {
      color: #f98181;
    }

    .hljs-number,
    .hljs-meta,
    .hljs-built_in,
    .hljs-builtin-name,
    .hljs-literal,
    .hljs-type,
    .hljs-params {
      color: #fbbc88;
    }

    .hljs-string,
    .hljs-symbol,
    .hljs-bullet {
      color: #b9f18d;
    }

    .hljs-title,
    .hljs-section {
      color: #faf594;
    }

    .hljs-keyword,
    .hljs-selector-tag {
      color: #70cff8;
    }

    .hljs-emphasis {
      font-style: italic;
    }

    .hljs-strong {
      font-weight: 700;
    }
  }
}

.tableWrapper {
  overflow-x: auto;
}

.resize-cursor {
  cursor: ew-resize;
  cursor: col-resize;
}

#theme-icon {
    position: absolute;
    right: 5%;
    top: -100%;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 50px;
    height: 50px;
    z-index: 2;
  }
  
  #sun-icon {
  position: absolute;
  width: 70px;
  height: 70px;
  top:-5px;
  }

  #moon-icon {
  position: absolute;
  width: 50px;
  height: 50px;
  top:0px;
  }



/* 太阳移动的动画 */
@keyframes Sun-disappear {
  0% {
    transform: translateY(115%);
  }
  100% {
    transform: translateY(0);
  }
}

@keyframes Sun-appear {
  0% {
    transform: translateY(0);
  }
  100% {
    transform: translateY(115%);
  }
}

/* 月亮移动的动画 */
@keyframes Moon-disappear{
  0% {
    transform: translateY(160%);
  }
  100% {
    transform: translateY(0);
  }
}

@keyframes Moon-appear{
  0% {
    transform: translateY(0);
  }
  100% {
    transform: translateY(160%);
  }
}

/* 太阳从显示到隐藏 */
.hide-sun {
  animation: Sun-disappear 0.3s  forwards;
}

/* 太阳从隐藏到显示 */
.show-sun {
  animation: Sun-appear 0.3s  forwards;
}

/* 月亮从显示到隐藏 */
.hide-moon {
  animation: Moon-disappear 0.3s  forwards; 
}

/* 月亮从隐藏到显示 */
.show-moon {
  animation: Moon-appear 0.3s   forwards;
}

@media (max-width: 700px) {
  .lefttop img {
    height: 30px;
    width: auto;
  }
}

@media (max-width: 1480px) {
  .topBtn{
    font-size: 12px;
  }
}
@media (max-width: 1400px) {
  .topBtn{
    font-size: 10px;
  }
}
@media (max-width: 1340px) {
  .editorcard {

  grid-template-rows: 8% 81% 4%;

}
}

@media (max-width: 1100px) {
  .topBtn{
    font-size: 8px;
  }
}

@media (max-height: 700px) {
  .lefttop img {
    height: 30px;
    width: auto;
  }
  #theme-icon {
    display: none;
  }
}

@media (max-height: 300px) {
  .lefttop img {
    display: none;
  }
}
</style>
