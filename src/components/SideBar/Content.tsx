import { FC, PropsWithChildren } from 'react'
import {
  Box,
  CloseButton,
  Flex,
  useColorModeValue,
  Text,
  BoxProps,
} from '@chakra-ui/react'


type Props = BoxProps & {
  onClose: () => void
}

export const SidebarContent: FC<PropsWithChildren<Props>> = (props) => {
  const { onClose, children, ...rest } = props
  return (
    <Box
      bg={useColorModeValue('white', 'gray.900')}
      borderRight="1px"
      borderRightColor={useColorModeValue('gray.200', 'gray.700')}
      w={{ base: 'full', md: 60 }}
      pos="fixed"
      h="full"
      {...rest}>
      <Flex h="20" alignItems="center" mx="8" justifyContent="space-between">
        <Text fontSize="2xl" fontFamily="monospace" fontWeight="bold">
          Logo
        </Text>
        <CloseButton display={{ base: 'flex', md: 'none' }} onClick={onClose} />
      </Flex>
      {children}
    </Box>
  )
}
