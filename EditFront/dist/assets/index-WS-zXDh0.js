import{a as k}from"./axios-B4uVmeYG.js";import{m as x}from"./index-BjJ2-QAr.js";import{L as w}from"./Loading-CtJha2Rr.js";import{d as z,r as n,k as A,o as t,c as s,b as o,z as C,m as I,F as m,t as L,x as B,p as F,i as S,_ as D}from"./index-DuB4n2yr.js";const u=c=>(F("data-v-20ae9906"),c=c(),S(),c),M={class:"file-manager"},V={class:"add-file"},E=u(()=>o("h2",null,"OCR图片识别",-1)),T=u(()=>o("path",{d:"M576 928H192c-52.992 0-96-43.093333-96-96V192c0-52.992 43.093333-96 96-96h640c52.992 0 96 43.093333 96 96v384.064c0 17.706667-14.293333 32-32 32s-32-14.293333-32-32V192.021333c0-17.706667-14.4-32-32-32H192c-17.706667 0-32 14.378667-32 32v639.957334c0 17.706667 14.4 32 32 32h384c17.706667 0 32 14.314667 32 32 0 17.706667-14.293333 32.021333-32 32.021333zM128 693.312a32.064 32.064 0 0 1-22.613333-54.698667l159.402666-159.338666a95.786667 95.786667 0 0 1 110.72-17.984l173.589334 86.805333c12.309333 6.186667 27.093333 3.797333 36.8-5.994667l287.402666-287.445333a32.042667 32.042667 0 0 1 45.290667 45.312L631.210667 587.392a95.786667 95.786667 0 0 1-110.72 18.005333l-173.589334-86.826666a31.616 31.616 0 0 0-36.8 6.016l-159.509333 159.317333c-6.186667 6.314667-14.4 9.386667-22.592 9.386667z m320-277.376c-52.906667 0-96-43.093333-96-96s43.093333-96.021333 96-96.021333 96 43.093333 96 96-43.093333 96.021333-96 96.021333z m0-128c-17.6 0-32 14.378667-32 32 0 17.6 14.4 32 32 32s32-14.4 32-32c0-17.621333-14.4-32-32-32zM768 928c-17.706667 0-32-14.293333-32-32v-192.021333c0-17.706667 14.293333-32 32-32s32 14.293333 32 32v192c0 17.706667-14.293333 32.021333-32 32.021333z m128-128c-7.893333 0-15.701333-2.922667-21.909333-8.725333L768 691.669333l-106.090667 99.712a31.936 31.936 0 0 1-45.226666-1.408 31.957333 31.957333 0 0 1 1.408-45.205333l112.213333-105.386667A48.554667 48.554667 0 0 1 768 621.44c14.72 0 28.501333 6.613333 37.696 17.92l112.213333 105.386667A31.957333 31.957333 0 0 1 896 800z",fill:"#8a8a8a","p-id":"3651"},null,-1)),H=[T],N={class:"loadingarea"},R={class:"content"},b={key:0},O={key:1},P=z({__name:"index",setup(c){const h=n(""),r=x(),d=n([]),p=n(null),l=n([]),i=n(!1),_=()=>{var a;(a=p.value)==null||a.click()},f=a=>{const e=a.target;e.files&&(d.value=Array.from(e.files),g())},g=()=>{i.value=!0;let a=new FormData;a.append("username",r.username),d.value.forEach(e=>{a.append("img",e,"img.png"),console.log("Added file to formData:",e)}),k({method:"post",url:`${r.ipAddress}/api/img2word`,data:a,headers:{"Content-Type":"multipart/form-data"}}).then(e=>{console.log("Response received:",e),e.data&&e.data.ret===1?alert("上传失败"):e.data&&Array.isArray(e.data.res)?(l.value=e.data.res,console.log("Parsed response data.res:",l.value)):(console.error("Unexpected response format:",e.data),l.value=[])}).catch(e=>{console.error("Error during image upload:",e),alert("上传过程中发生错误")}).finally(()=>{i.value=!1})};return A(()=>{r.initializeTheme(),h.value=r.theme}),(a,e)=>(t(),s(m,null,[o("div",M,[o("div",V,[E,(t(),s("svg",{onClick:_,t:"1719546222308",class:"icon",viewBox:"0 0 1024 1024",version:"1.1",xmlns:"http://www.w3.org/2000/svg","p-id":"3650",width:"200",height:"200"},H))]),o("input",{type:"file",ref_key:"fileInput",ref:p,onChange:f,multiple:"",hidden:""},null,544)]),o("div",N,[i.value?(t(),C(w,{key:0})):I("",!0)]),o("div",R,[l.value.length>0?(t(),s("ul",b,[(t(!0),s(m,null,L(l.value,(v,y)=>(t(),s("li",{key:y},B(v),1))),128))])):(t(),s("p",O,"没有识别到内容"))])],64))}}),G=D(P,[["__scopeId","data-v-20ae9906"]]);export{G as default};