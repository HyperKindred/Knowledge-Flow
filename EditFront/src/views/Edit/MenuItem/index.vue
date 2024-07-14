<template>
  <button
    class="menu-item"
    :class="{ 'is-active': props.isActive ? props.isActive() : null }"
    @click="props.action"
    :title="props.title"
  >
    <svg v-if="props.iconType === 'remix'" class="remix">
      <use :xlink:href="`${remixiconUrl}#ri-${props.icon}`" />
    </svg>
    <template v-else-if="props.iconType === 'custom'">
      <svg t="1720926979138" class="markdown" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4323" width="256" height="256"><path d="M85.333333 682.666667 85.333333 341.333333 170.666667 341.333333 298.666667 469.333333 426.666667 341.333333 512 341.333333 512 682.666667 426.666667 682.666667 426.666667 462.08 298.666667 590.08 170.666667 462.08 170.666667 682.666667 85.333333 682.666667M682.666667 341.333333 810.666667 341.333333 810.666667 512 917.333333 512 746.666667 704 576 512 682.666667 512 682.666667 341.333333Z" p-id="4324"></path></svg>
    </template>
  </button>
</template>

<script setup lang="ts">
import remixiconUrl from 'remixicon/fonts/remixicon.symbol.svg'
const props = defineProps<{
  icon: string
  title: string
  action: Function
  isActive?: Function
  iconType?: string
}>()
</script>

<style lang="scss">
.menu-item {
  background: transparent;
  border: none;
  border-radius: 0.4rem;
  color: var(--btnColor);
  cursor: pointer;
  height: 1.75rem;
  padding: 0.25rem;
  margin-right: 0.25rem;
  width: 1.75rem;


  svg {
    fill: currentColor;
    height: 100%;
    width: 100%;
  }

  &.is-active,
  &:hover {
    background-color: var(--titleColor);
  }
}


</style>
