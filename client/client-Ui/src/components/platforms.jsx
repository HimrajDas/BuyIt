import React from 'react'
import styled from 'styled-components'
import { edtechPlatforms } from '../data'
import Platform from './platform'

const Container = styled.div`
  padding: 20px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
`

const Platforms = () => {
  return (
    <Container>
      {edtechPlatforms.map((item) => (
        <Platform item={item} key={item.id} />
      ))}
    </Container>
  )
}
export default Platforms