import{d as h,r as l,H as v,k as x,o as p,c as y,b as e,z as w,m as k,w as z,v as S,E as i,p as b,i as B,_ as C}from"./index-DuB4n2yr.js";import{a as D}from"./axios-B4uVmeYG.js";import{m as E}from"./index-BjJ2-QAr.js";import{L as I}from"./Loading-CtJha2Rr.js";const L=r=>(b("data-v-2a91f4d3"),r=r(),B(),r),T={class:"container"},M=L(()=>e("div",{class:"title"},[e("h2",null,"文本摘要")],-1)),V={class:"text-item"},N={class:"loadingarea"},A=h({__name:"index",setup(r){const n=l(""),t=E(),u=l(""),c=l(!1),m=a=>{let s=new FormData;s.append("text",a),D({method:"post",url:`${t.ipAddress}/api/summarize`,data:s,headers:{"Content-Type":"multipart/form-data"}}).then(o=>{let d=o.data;d.ret===0?n.value=d.res:i({message:"摘要失败："+d.msg,type:"error",duration:5*1e3,grouping:!0})}).catch(o=>{console.error("Error posting data:",o),i({message:"摘要失败：网络错误，请稍后重试！",type:"error",duration:5*1e3,grouping:!0})}).finally(()=>{f()})};v(()=>t.select,a=>{a==="summarize"&&(_(),m(t.content))});const g=async()=>{try{await navigator.clipboard.writeText(n.value),i({message:"内容已复制到剪切板! ",type:"success",duration:5*1e3,grouping:!0})}catch{i({message:"复制失败，请重试! ",type:"error",duration:5*1e3,grouping:!0})}};x(()=>{t.initializeTheme(),u.value=t.theme});const _=()=>{c.value=!0},f=()=>{c.value=!1};return(a,s)=>(p(),y("div",T,[M,e("div",V,[e("div",N,[c.value?(p(),w(I,{key:0})):k("",!0),z(e("textarea",{class:"textarea","onUpdate:modelValue":s[0]||(s[0]=o=>n.value=o),placeholder:"摘要结果"},null,512),[[S,n.value]])]),e("button",{class:"button",onClick:g},"复制")])]))}}),j=C(A,[["__scopeId","data-v-2a91f4d3"]]);export{j as default};