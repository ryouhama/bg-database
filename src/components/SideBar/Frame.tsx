import { FC, PropsWithChildren } from 'react'
import { useColorModeValue, Box, Drawer, DrawerContent } from '@chakra-ui/react'


type Props = {
  isOpen: boolean
  onClose: () => void
}

export const SideBarFrame: FC<PropsWithChildren<Props>> = (props) => {
  const { isOpen, onClose, children } = props
  return (
    <Box minH="100vh" bg={useColorModeValue('gray.100', 'gray.900')}>
      <Drawer
        isOpen={isOpen}
        placement="left"
        onClose={onClose}
        returnFocusOnClose={false}
        onOverlayClick={onClose}
        size="full">
        <DrawerContent>
          {children}
        </DrawerContent>
      </Drawer>
    </Box>
  )
}